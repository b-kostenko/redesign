import jwt
from typing import final
from datetime import datetime, timedelta, timezone
from typing import Dict, Any

from app.config.settings import settings
from app.domain import entities
from app.domain.entities.auth import TokenType
from app.domain.interfaces.security import TokenServiceInterface


@final
class JwtTokenService(TokenServiceInterface):
    def __init__(self):
        self._secret_key = settings.token.SECRET_KEY
        self._algorithm = settings.token.ALGORITHM

    def generate_tokens_for_user(self, user: entities.User) -> entities.Token:
        access_token = self.create_token(
            payload={"sub": user.email},
            token_type=TokenType.ACCESS,
            expire_minutes=settings.token.ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        refresh_token = self.create_token(
            payload={"sub": user.email},
            token_type=TokenType.REFRESH,
            expire_minutes=settings.token.REFRESH_TOKEN_EXPIRE_MINUTES,
        )

        return entities.Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type=settings.token.TOKEN_TYPE
        )

    def create_token(self, payload: dict, token_type: TokenType, expire_minutes: int) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
        data = payload | {"exp": expire, "type": token_type}
        return jwt.encode(data, self._secret_key, algorithm=self._algorithm)

    def decode_token(self, token: str) -> dict:
        return jwt.decode(
            token,
            self._secret_key,
            algorithms=[self._algorithm],
        )

    def verify_token(self, token: str, token_type: TokenType) -> Dict[str, Any]:
        payload = self.decode_token(token)
        if payload.get("type") != token_type:
            raise ValueError("Invalid token type")
        return payload

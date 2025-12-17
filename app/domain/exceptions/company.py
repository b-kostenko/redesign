from app.domain.exceptions import base


class CompanyAlreadyExistsError(base.AlreadyExistsError):
    def __init__(self, name: str):
        super().__init__(f"Company with name '{name}' already exists")


class CompanyNotFoundError(base.NotFoundError):
    def __init__(self, company_attr: str | int):
        super().__init__(f"Company with identifier '{company_attr}' not found")


class CompanyMismatchError(base.ValidationError):
    def __init__(self, user_company_id: int, current_company_id: int):
        super().__init__(
            f"User company id '{user_company_id}' does not match current company id '{current_company_id}'"
        )

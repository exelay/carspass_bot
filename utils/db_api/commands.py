from asyncpg import UniqueViolationError

from utils.db_api.schemas.user import User


async def add_user(id: int, phone: str, code: str):
    try:
        user = User(id, phone, code)
        await user.create()
    except UniqueViolationError:
        pass

from asyncpg import UniqueViolationError

from utils.db_api.schemas.user import User


async def add_user(id_: int, phone: str, code: str):
    try:
        user = User(id=id_, phone=phone, pass_code=code)
        await user.create()
    except UniqueViolationError:
        pass

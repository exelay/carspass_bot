from loader import db
from utils.db_api import db_gino


async def on_startup(dp):
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()
    print("Готово")


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

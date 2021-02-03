from loader import db


async def on_startup(dp):
    try:
        db.create_table_users()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

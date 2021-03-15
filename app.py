from loguru import logger
from sqlite3 import OperationalError

from loader import db
from utils.notify_admins import on_startup_notify
from utils.set_default_commands import set_default_commands


async def on_startup(dp):
    logger.add('debug.log', level='DEBUG', rotation='100 KB', compression='zip')
    logger.info('Creating tables...')
    try:
        db.create_table_users()
        logger.info('Table successfully created!')
    except OperationalError:
        logger.info('Table already exists!')
    except Exception as err:
        logger.error(f'Table creation error: {err}')

    # await on_startup_notify(dp, db)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

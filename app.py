from loguru import logger

from loader import db
from utils.notify_admins import on_startup_notify


async def on_startup(dp):
    logger.add('debug.log', level='DEBUG', rotation='10 KB', compression='zip')
    try:
        logger.info('Creating tables...')
        db.create_table_users()
    except Exception as err:
        logger.error(f'Table creation error: {err}')
    else:
        await on_startup_notify(dp)
        logger.info('Table successfully created!')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

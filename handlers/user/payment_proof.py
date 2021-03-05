from loguru import logger
from aiogram import types

from loader import dp
from data.config import ADMINS
from utils.notify_admins import error_notify


@dp.callback_query_handler(text='paid')
async def paid_handler(callback: types.CallbackQuery):
    try:
        user_id = callback.from_user.id
        text = (
            "#for_admins\n"
            f"Пользователь <code>{user_id}</code> подтвердил оплату."
        )
        for admin in ADMINS:
            await dp.bot.send_message(admin, text)
        await dp.bot.send_message(user_id, 'Заявка на подтверждение отправлена, ожидайте.')
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")

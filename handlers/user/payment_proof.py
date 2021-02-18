from loguru import logger
from aiogram import types

from loader import dp, db
from data.config import ADMINS
from utils.notify_admins import error_notify


@dp.callback_query_handler(text='paid')
async def paid_handler(callback: types.CallbackQuery):
    try:
        user_id = callback.from_user.id
        phone = db.select_user(id=user_id)[1]
        text = (
            "#for_admins\n"
            f"Пользователь с номером <code>+{phone}</code> подтвердил оплату."
        )
        for admin in ADMINS:
            await dp.bot.send_message(admin, text)
        await dp.bot.send_message(user_id, 'Заявка на подтверждение отправлена, ожидайте.')
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")


@dp.message_handler(commands=['paid'])
async def show_paid_button(message: types.Message):
    try:
        text = "Нажми на кнопку, чтобы подтвердить оплату."
        markup = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("Подтвердить оплату", callback_data="paid")
        )
        await message.answer(text, reply_markup=markup)
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")


@dp.message_handler()
async def proof_payment(message: types.Message):
    try:
        if message.text == "💵Подтвердить оплату💵":
            user_id = message.from_user.id
            phone = db.select_user(id=user_id)[1]
            text = (
                "#for_admins\n"
                f"Пользователь с номером <code>+{phone}</code> хочет подтвердить оплату."
            )
            for admin in ADMINS:
                await dp.bot.send_message(admin, text)
            await message.answer('Заявка на подтверждение отправлена, ожидайте.')
        else:
            pass
    except Exception as err:
        await error_notify(dp, err)
        logger.error(f"Something went wrong: {err}")

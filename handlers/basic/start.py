from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from messages import MESSAGES
from keyboards import start_markup


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    try:
        auth_code = message.text.split()[1]
    except IndexError:
        auth_code = None
    if auth_code:
        text = MESSAGES['hello'].format(user_name)
        # Отправить запрос на сервер
    else:
        text = MESSAGES['not_hello'].format(user_name)
    await message.answer(text, reply_markup=start_markup)

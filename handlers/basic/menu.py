from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from loader import dp
from keyboards import menu_markup


@dp.message_handler(Command('menu'))
async def menu_command(message: Message):
    await message.answer("Меню", reply_markup=menu_markup)


@dp.callback_query_handler(text='menu')
async def menu_handler(callback: CallbackQuery):
    await callback.message.answer("Меню", reply_markup=menu_markup)

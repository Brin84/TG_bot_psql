from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from database.utils import db_register_user

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    """Реакция на команду /start"""
    await message.answer(
        f'Привет, <i>{message.from_user.full_name}</i>',
        parse_mode='HTML'
    )
    await register_user(message)


async def register_user(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    if db_register_user(chat_id, full_name):
        await message.answer(
            f'Привет, {full_name}, я запомнил тебя!'
        )

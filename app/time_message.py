from aiogram import Bot
from aiogram.types import Message


async def send_message(bot: Bot, message: Message):
    await bot.send_message(message.chat.id, 'Сообщение через несколько секунд')
import asyncio
import os 
import sys 
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ChatJoinRequest
from aiogram import BaseMiddleware
import datetime as dt
from aiogram.enums import ChatType, ContentType
#нужно установить пакет apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import types
from aiogram.methods import GetChatMember

import app.keyboards as kb
from app.handlers import router

#в переменных среды нужно указать телeграм токен
TOKEN = '6809644257:AAHqH8eW6YtJ-8UE_IdIPr-G_zMtc_DMst0'



## позволяет доставать scheduler из агрументов фунции
class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler):
        super().__init__()
        self._scheduler = scheduler

    async def __call__(self,handler,event,data):
        # прокидываем в словарь состояния scheduler
        data["scheduler"] = self._scheduler
        return await handler(event, data)



@router.message(Command(commands=["start"]))
# middleware просовывает для нас sheduler в аргументы функции 
async def hello(message:Message, bot: Bot, scheduler: AsyncIOScheduler):
    # получаем id, обратившегося к боту
    id = message.from_user.id
    user_channel_status = await bot.get_chat_member(chat_id='-1002105665067', user_id=id)
    if user_channel_status.status != 'left':
        await message.answer_photo(photo='AgACAgIAAxkBAAPTZhlH8TKe7JAfwgUd75SUFGNyb6MAAg7YMRvTcslILq8PLuEOFQcBAAMCAAN4AAM0BA', caption='Congratulations, my friend ' + str(message.from_user.first_name) + '!🥇\n\n'
                               f'Finally you found a real Guru!😌\n'
                               f'I will teach you how to make money just playing simple slot games. \n\n'
                               f'<b>Subscribe</b> to <b>my channel</b> to find out how to make money\n'
                               f'If you want to earn money right now, press START👇🏼', parse_mode='html',disable_web_page_preview=1,
                               reply_markup=kb.main)
    else:
        await bot.send_message(message.from_user.id, 'Подпишитесь на канал по ссылке https://t.me/+6K2Do5ZHIQoxOGJi')
    



# async def send_message_to_subscribers(bot: Bot, channel_id: str, message_text: str):
#     # Создайте экземпляр объекта GetChatMember, указав идентификатор чата и пользователя
#     get_chat_member = GetChatMember(chat_id='-1002105665067', user_id=member_id)
#     # Отправьте запрос на сервер Telegram, чтобы получить информацию о пользователе в чате
#     chat_member = await bot.get_chat_member(chat_id=get_chat_member.chat_id, user_id=get_chat_member.user_id)
#     # Получаем количество участников канала
#     members_count = await bot.get_chat_members_count(channel_id)
#     for member_id in range(members_count):
#         try:
#             # Получаем информацию о каждом участнике
#             member = await bot.get_chat_member(channel_id, member_id)
#             # Проверяем, что это пользователь, а не бот или другой тип участника
#             if member.user:
#                 # Отправляем личное сообщение каждому подписчику
#                 await bot.send_message(member.user.id, message_text)
#         except Exception as e:
#             # Обработка возможных ошибок при отправке сообщения
#             print(f"Error sending message to {member.user.id}: {e}")

async def main():
    # для работы с временем нужно указывать часовой пояс. По дефолту Лондон :)
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.start()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(router)
    # регистрируем middleware c scheduler
    dp.update.middleware(
        SchedulerMiddleware(scheduler=scheduler),
    )
    
    # await send_message_to_subscribers(
    # bot,
    # channel_id='-1002105665067',  # ID вашего канала
    # message_text='Привет! Это сообщение отправлено вам из бота.'
    # )
    
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    asyncio.run(main())

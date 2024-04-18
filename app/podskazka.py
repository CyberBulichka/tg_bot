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

#нужно установить пакет apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler


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
    await message.answer_photo(photo='AgACAgIAAxkBAAPTZhlH8TKe7JAfwgUd75SUFGNyb6MAAg7YMRvTcslILq8PLuEOFQcBAAMCAAN4AAM0BA', caption='Congratulations, my friend ' + str(message.from_user.first_name) + '!🥇\n\n'
                               f'Finally you found a real Guru!😌\n'
                               f'I will teach you how to make money just playing simple slot games. \n\n'
                               f'<b>Subscribe</b> to <b>my channel</b> to find out how to make money\n'
                               f'If you want to earn money right now, press START👇🏼', parse_mode='html',disable_web_page_preview=1,
                               reply_markup=kb.main)

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
    
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    asyncio.run(main())

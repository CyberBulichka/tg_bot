from aiogram.types import Message, CallbackQuery, ChatJoinRequest
from aiogram.filters import CommandStart, Command
from aiogram import F, Router, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.methods import SendMessage
from apscheduler.schedulers.asyncio import AsyncIOScheduler



import app.keyboards as kb

router = Router()
chat_id = -1002105665067
bot = Bot(token='6809644257:AAHqH8eW6YtJ-8UE_IdIPr-G_zMtc_DMst0')

    
    
@router.callback_query(F.data == 'nachalo')
async def nachalo(callback: CallbackQuery):
    # await callback.answer('Любая необходимая информация, в том числе ссылка на сайт', show_alert=True)
    await callback.message.answer('Привет')
    

@router.chat_join_request()
async def start1(update: ChatJoinRequest):
    
    # тут мы принимаем юзера в канал
    await update.approve()
    # а тут отправляем сообщение
    await bot.send_message(chat_id=update.from_user.id, text='Я рад, что Вы подписались на наш канал!\nДля получения самых свежих новостей с нашего канала', parse_mode='html',disable_web_page_preview=1,)

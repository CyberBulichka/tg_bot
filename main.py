import asyncio
from aiogram import Bot, Dispatcher, types

from app.handlers import router



async def main():
    bot = Bot(token='6809644257:AAHqH8eW6YtJ-8UE_IdIPr-G_zMtc_DMst0')
    dp = Dispatcher()
    dp.include_router(router)
    CHANNEL_ID = -1002105665067
    ADMIN_ID = 6809644257
    await dp.start_polling(bot)
    
@router.chat_join_request_handler()
async def start1(update: types.ChatJoinRequest):
    # тут мы принимаем юзера в канал
    await update.approve()
    # а тут отправляем сообщение
    await router.send_message(chat_id=update.from_user.id, text="текст сообщения бота в лс юзеру")
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен') 
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router, types


import app.keyboards as kb

router = Router()


@router.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer('Для демонстрации функционала Инлайн клавиатуры, нажмите кнопку Старт', reply_markup=kb.main)
async def cmd_start(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAPTZhlH8TKe7JAfwgUd75SUFGNyb6MAAg7YMRvTcslILq8PLuEOFQcBAAMCAAN4AAM0BA', caption='Congratulations, my friend ' + str(message.from_user.first_name) + '!🥇\n\n'
                               f'Finally you found a real Guru!😌\n'
                               f'I will teach you how to make money just playing simple slot games. \n\n'
                               f'<b>Subscribe</b> to <b>my channel</b> to find out how to make money\n'
                               f'If you want to earn money right now, press START👇🏼', parse_mode='html',disable_web_page_preview=1,
                               reply_markup=kb.main)
    print(message.chat.id)
    
    
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')
    
@router.callback_query(F.data == 'nachalo')
async def nachalo(callback: CallbackQuery):
    await callback.answer('Любая необходимая информация, в том числе ссылка на сайт', show_alert=True)
    await callback.message.answer('Вы выбрали START!')
    

# @router.message(F.photo)
# async def photo_handler(message: Message) -> None:
#     photo_data = message.photo[-1]
#     await message.answer(f'{photo_data}')

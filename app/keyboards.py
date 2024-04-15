from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

# main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Старт')],
#                                      [KeyboardButton(text='Проверка')],
#                                      [KeyboardButton(text='Отмена')]],
#                            resize_keyboard=True,
#                            input_field_placeholder='Выберите пункт меню...')



main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='START!', callback_data='nachalo')],
    [InlineKeyboardButton(text='WRITE ME', callback_data='sviaz')]])
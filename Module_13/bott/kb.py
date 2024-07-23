from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
    ], resize_keyboard=True
)


inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(callback_data="calories", text="Рассчитать норму калорий", ),
         InlineKeyboardButton(callback_data="formulas", text="Формулы расчёта", )],
    ]
)


sex_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мужчина"),
         KeyboardButton(text="Женщина")],
    ], resize_keyboard=True
)

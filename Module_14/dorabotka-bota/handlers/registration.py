from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from crud_functions import *
import kb


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):",
                         reply_markup=types.ReplyKeyboardRemove())
    await RegistrationState.username.set()


async def set_username(message, state):
    if is_included(message.text):
        await message.answer("Пользователь уже существует, введите другое имя:")
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


async def set_email(message, state):
    if not is_correct_email(message.text):
        await message.answer("Некорректный email, попробуйте ещё раз:")
    else:
        await state.update_data(email=message.text)
        await message.answer("Введите свой возраст:")
        await RegistrationState.age.set()


async def set_age(message, state):
    if not message.text.isdigit():
        await message.answer("Введите свой возраст ЦИФРАМИ:")
    else:
        await state.update_data(age=message.text)
        data = await state.get_data()
        username, email, age = (data["username"], data["email"], int(data["age"]))
        add_user(username, email, age)
        await message.answer("Регистрация успешно завершена!", reply_markup=kb.start_kb)
        await state.finish()

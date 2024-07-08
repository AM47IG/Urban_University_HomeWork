from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from config_reader import config

api = config.bot_token.get_secret_value()
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    address = State()


@dp.message_handler(text=['Привет'])
async def all_message(message):
    print("Мы получили сообщение!")


@dp.message_handler(text=["Urban"])
async def urban_message(message):
    print("Urban message")
    await message.answer("Urban message")


@dp.message_handler(commands='start')
async def start_message(message):
    print('Start message')
    await message.answer('Рады видеть Вас в нашем Боте!')


@dp.message_handler(text='Заказать')
async def buy(message):
    await message.answer("Отправь нам свой адрес, пожалуйста")
    await UserState.address.set()


@dp.message_handler(state=UserState.address)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f'Доставка будет отправлена по адресу {data["first"]}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение!')
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
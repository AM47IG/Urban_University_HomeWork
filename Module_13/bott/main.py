import asyncio
import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import kb
from config_reader import config

api = config.bot_token.get_secret_value()
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    sex = State()
    age = State()
    age_incorrect = State()
    growth = State()
    weight = State()


@dp.message_handler(commands="start")
async def start(message):
    # print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb.start_kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb.inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        "для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"
        "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161"
    )
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_sex_inline(call):
    await call.message.answer("Выберите свой пол:", reply_markup=kb.sex_kb)
    await call.answer()
    await UserState.sex.set()


@dp.message_handler(text='calories')
async def set_sex(message):
    await message.answer("Выберите свой пол:", reply_markup=kb.sex_kb)
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    if message.text not in ["Мужчина", "Женщина"]:
        await message.answer("Выберите свой пол КНОПКАМИ:", reply_markup=kb.sex_kb)
    else:
        await state.update_data(sex=message.text)
        await message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())
        await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if not message.text.isdigit():
        await message.answer("Введите свой возраст ЦИФРАМИ:")
    else:
        await state.update_data(age=message.text)
        await message.answer("Введите свой рост:")
        await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if not message.text.isdigit():
        await message.answer("Введите свой рост ЦИФРАМИ:")
    else:
        await state.update_data(growth=message.text)
        await message.answer("Введите свой вес:")
        await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if not message.text.isdigit():
        await message.answer("Введите свой вес ЦИФРАМИ:")
    else:
        await state.update_data(weight=message.text)
        data = await state.get_data()
        s = data['sex']
        w, g, a = map(int, (data["weight"], data["growth"], data["age"]))
        if s == 'Мужчина':
            result = 10 * w + 6.25 * g - 5 * a + 5  # Для мужчин
        else:
            result = 10 * w + 6.25 * g - 5 * a - 161  # Для женщин
        await message.answer(f'Ваша норма калорий в сутки {result:.2f}', reply_markup=kb.start_kb)
        await state.finish()


@dp.message_handler()
async def all_message(message):
    # print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # executor.start_polling(dp, skip_updates=True)
    executor.start_polling(dp, allowed_updates=["message", "edited_channel_post", "callback_query", "edited_message",
                                                "channel_post", "edited_channel_post", "inline", "chosen_inline",
                                                "shipping_query", "pre_checkout_query", "poll", "poll_answer",
                                                "my_chat_member", "chat_member", "chat_join_request", "errors", ])

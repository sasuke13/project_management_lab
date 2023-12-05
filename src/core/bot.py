import json
import os
import io

import aiohttp
from aiohttp import ClientConnectorError
from dotenv import load_dotenv

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

load_dotenv()

bot = Bot(os.environ.get('TELEGRAM_BOT_KEY'))
dp = Dispatcher(bot)

#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     engine = db.create_engine(db_url)
#
#     conn = engine.connect()
#     output = conn.execute("SELECT * FROM public.core_botadmins")
#     print(output.fetchall())
    # user = await BotAdmins.objects.get(message.from_user.username)

    # if user:
    #     await bot.send_message(message.from_user.id, message.from_user.username)
    #
    # else:
    #     await bot.send_message(message.from_user.id, message.from_user.first_name)


@dp.message_handler(commands=['inner_menu'])
async def inner_menu_handler(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(
                "Get all statistic",
                callback_data="Statistic_?"
            )
        ],
        [
            types.InlineKeyboardButton(
                "Get all orders in range of the month",
                callback_data="Statistic_?days=30"
            )
        ],
        [
            types.InlineKeyboardButton(
                "Get all new orders in range of the month",
                callback_data="Statistic_?days=30&state=NW"
            )
        ],
        [
            types.InlineKeyboardButton(
                "Get all cancelled orders in range of the month",
                callback_data="Statistic_?days=30&state=CNL"
            )
        ],
        [
            types.InlineKeyboardButton(
                "Get count of orders in range of the month",
                callback_data="Count_?days=30"
            )
        ],
        [
            types.InlineKeyboardButton(
                "Get count of new orders in range of the month",
                callback_data="Count_?days=30&state=NW"
            )
        ],
        [
            types.InlineKeyboardButton(
                "Get count of cancelled orders in range of the month",
                callback_data="Count_?days=30&state=CNL"
            )
        ]
    ])
    await message.answer("Inner menu", reply_markup=inline_keyboard)


@dp.callback_query_handler(text_contains="Statistic")
async def hello_callback_handler(callback: types.CallbackQuery):
    endpoint_data = callback.data.split('_')[1]
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://localhost:8000/api/v1/orders/statistic/{endpoint_data}') as resp:
                if resp.status == 200:
                    file_obj = io.BytesIO()
                    file_obj.write((json.dumps(await resp.json(), indent=2)).encode())
                    file_obj.seek(0)

                    await callback.message.answer_document(document=file_obj)
                else:
                    await callback.message.answer(text=f'Server responded with a status code {resp.status}')

    except ClientConnectorError:
        await callback.message.answer(text='Error connecting to the server. Please try again later.')


@dp.callback_query_handler(text_contains="Count")
async def hello_callback_handler(callback: types.CallbackQuery):
    endpoint_data = callback.data.split('_')[1]
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://localhost:8000/api/v1/orders/statistic/{endpoint_data}') as resp:
                if resp.status == 200:
                    await callback.message.answer(str(len((await resp.json())['results'])))
                else:
                    await callback.message.answer(text=f'Server responded with a status code {resp.status}')

    except ClientConnectorError:
        await callback.message.answer(text='Error connecting to the server. Please try again later.')


executor.start_polling(dp)

import os

from core.middleware import AuthMiddleWare
from core.storage import add_user_to_session

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
from django.conf import settings

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

if not settings.configured:
    django.setup()

import json
import io

import aiohttp
from aiohttp import ClientConnectorError
from dotenv import load_dotenv

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from core.models import BotAdmins

load_dotenv()

bot = Bot(os.environ.get('TELEGRAM_BOT_KEY'))
dp = Dispatcher(bot)
dp.middleware.setup(AuthMiddleWare())

current_page = 0


async def get_menu_page(page):
    if page == 0:
        return [
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
            ],
            [
                types.InlineKeyboardButton(
                    "Next Page",
                    callback_data="Next Page"
                )
            ],
        ]
    elif page == 1:
        return [
            [
                types.InlineKeyboardButton(
                    "Get all orders in range of the half of year",
                    callback_data="Statistic_?days=180"
                )
            ],
            [
                types.InlineKeyboardButton(
                    "Get all new orders in range of half of year",
                    callback_data="Statistic_?days=180&state=NW"
                )
            ],
            [
                types.InlineKeyboardButton(
                    "Get all cancelled orders in range of half of year",
                    callback_data="Statistic_?days=180&state=CNL"
                )
            ],
            [
                types.InlineKeyboardButton(
                    "Get count of orders in range of half of year",
                    callback_data="Count_?days=180"
                )
            ],
            [
                types.InlineKeyboardButton(
                    "Get count of new orders in range of half of year",
                    callback_data="Count_?days=180&state=NW"
                )
            ],
            [
                types.InlineKeyboardButton(
                    "Get count of cancelled orders in range of half of year",
                    callback_data="Count_?days=180&state=CNL"
                )
            ],
            [
                types.InlineKeyboardButton(
                    "Prev Page",
                    callback_data="Prev Page"
                )
            ],
        ]
    else:
        return []


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user = BotAdmins.objects.filter(tg_nickname=message.from_user.username).first()

    if user:
        await add_user_to_session(user.tg_nickname)
        await bot.send_message(
            message.from_user.id,
            f"Hello, {message.from_user.first_name}, what can I do for you?"
        )
    else:
        await bot.send_message(message.from_user.id, "You have no access to this bot!")


@dp.message_handler(commands=['inner_menu'])
async def inner_menu_handler(message: types.Message):
    global current_page
    current_page = 0
    inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=await get_menu_page(current_page))
    await message.answer("Inner menu", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda query: query.data.startswith("Next Page"))
async def next_page_handler(callback: types.CallbackQuery):
    global current_page
    current_page += 1
    inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=await get_menu_page(current_page))
    await callback.message.edit_reply_markup(reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda query: query.data.startswith("Prev Page"))
async def prev_page_handler(callback: types.CallbackQuery):
    global current_page
    if current_page > 0:
        current_page -= 1
    else:
        0
    inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=await get_menu_page(current_page))
    await callback.message.edit_reply_markup(reply_markup=inline_keyboard)


@dp.callback_query_handler(text_contains="Statistic")
async def statistic_callback_handler(callback: types.CallbackQuery):
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
async def count_callback_handler(callback: types.CallbackQuery):
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


if __name__ == "__main__":
    executor.start_polling(dp)

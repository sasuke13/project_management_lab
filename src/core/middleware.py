from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from core.storage import check_auth_user


class AuthMiddleWare(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        username = message.from_user.username
        if 'start' in message.text:
            return

        if not await check_auth_user(username):
            await message.answer('You have no access to this bot!')
            raise CancelHandler()

    async def on_pre_process_callback_query(self, callback: types.CallbackQuery, data: dict):
        username = callback.from_user.username

        if not await check_auth_user(username):
            await callback.answer('You have no access to this bot!')
            raise CancelHandler()

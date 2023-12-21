#!/usr/bin/env python

from aiogram.utils import executor

from src.core.bot import dp

if __name__ == "__main__":
    executor.start_polling(dp)

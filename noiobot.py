import asyncio
import sys
import time

from aiogram import executor

from noio.bot.polling import send_message
from noio.bot.service import dp


if sys.argv[1] == "bot":
    executor.start_polling(dp, skip_updates=True)

elif sys.argv[1] == "tasks":
    while True:
        asyncio.run(send_message())
        time.sleep(60)

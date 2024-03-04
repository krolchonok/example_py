import asyncio
import logging

from aiogram import Bot, Dispatcher, types

TOKEN = ""

dp = Dispatcher()

@dp.message()
async def echo_handler(message: types.Message) -> None:
    ...
  
async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

logging.basicConfig(level=logging.INFO)
asyncio.run(main())

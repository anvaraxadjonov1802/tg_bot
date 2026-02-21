from aiogram import Bot, Dispatcher, types
import os
import asyncio
from api import telegram_auth, get_products
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command('start'))
async def start_handel(message: types.Message):
    user = message.from_user

    data =  telegram_auth(user.id, user.full_name)
    token = data["access_token"]

    products = get_products(token)

    text = "📦 Mahsulotlar"
    for product in products:
        text += f" - {product["name"] - product["price"]} so'm\n"

    await message.answer(text)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


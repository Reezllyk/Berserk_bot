import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

import keyboards as kb

from dotenv import load_dotenv
import os

from crypto import get_btc_price

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Выберите действие:", reply_markup=kb.startMenu)

@dp.message(F.text == '⬅️ Назад')
async def backToMenu(message: Message):
    await message.answer(f"Выберите действие:", reply_markup=kb.startMenu)

@dp.message(F.text == '💵 Курс')
async def course(message: Message):
    price = await get_btc_price()
    if price:
        await message.answer(f"Текущий курс биткоина: <b>${price}</b> 💰")
    else:
        await message.answer("Не удалось получить курс биткоина 😢")

@dp.message(F.text == '☎️ Связь')
async def connection(message: Message):
    await message.answer('Нажми на кнопку для перехода в чат.', reply_markup=kb.urlsMenu)

@dp.message(F.text == '🚹 Информация')
async def connection(message: Message):
    await message.answer("Привет! Я <b>Berserk_bot</b>.🤖 Помогу тебе сориентироваться в ценах и связаться с автором.", reply_markup=kb.subMenu)


@dp.message(F.text.in_(['➡️ Меню', 'Меню']))
async def submenu(message:Message):
    await message.answer(f"Выберите действие:", reply_markup=kb.subMenu)


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = '6125679037:AAFR-QI02XQBZSWp6SNBvve6Z-uR4rF7U8E'  # Вставте свій токен тут

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привіт! Це тестовий бот.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

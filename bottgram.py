from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.storage import MemoryStorage
import openai
import os

# Встановлюємо ключі доступу
BOT_TOKEN = "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"
OPENAI_API_KEY = "5960019531:AAFjf2ENzHB2G2W_GpSAYlj_oQUVIXTbRJU"
openai.api_key = OPENAI_API_KEY

# Запускаємо бота
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Функція, яка відповідає на команду /start
async def start_command(message: types.Message):
    await message.answer("Привіт! Я бот, який може відповідати на твої запитання. Що тебе цікавить?")

# Зв'язуємо команду /start з функцією start_command()
dp.register_message_handler(start_command, commands=['start'])

# Функція, яка відповідає на звичайні текстові повідомлення
@dp.message_handler()
async def answer_question(message: types.Message):
    question = message.text
    answer = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Question: {question}\nAnswer:",
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=15,
    )
    await message.answer(answer.choices[0].text)

# Запускаємо бота відповідно до токену
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

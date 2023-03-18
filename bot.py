import openai
import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Встановлення токену бота
API_TOKEN = "6164487504:AAHeXobVmhTHpMd3sFRAda7BQAj2-LvPknY"

# Встановлення ключа API моделі ChatGPT
openai.api_key = "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"

# Створення екземпляру бота
bot = Bot(token="6164487504:AAHeXobVmhTHpMd3sFRAda7BQAj2-LvPknY")

# Створення диспетчера для обробки повідомлень
dp = Dispatcher(bot)


# Обробник повідомлень
@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_message(message: types.Message):
    # Отримання повідомлення від користувача
    question = message.text

    # Запит до моделі ChatGPT
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=15,
    )

    # Отримання відповіді від моделі
    answer = response.choices[0].text.strip()

    # Відправлення відповіді користувачу
    await message.reply(answer)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

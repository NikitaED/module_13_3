from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ':AAFuXa_bOkC4BBTUgFI-LToqpmchA_mxVUk'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handlers(commands = ['start'])
async def start(message):
        print('Привет! Я бот помогающий твоему здоровью.')
        await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handlers()
async def all_massages(message):
        print("Введите команду /start, чтобы начать общение.")
        await message.answer('Привет! Я бот помогающий твоему здоровью.')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


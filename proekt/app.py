import asyncio
import os
from aiogram import Bot, Dispatcher # импортирт класска BOT и Диспетчер

# Здесь подгрузка токена бота с помощью dotenv, хранится в отдельном файле .env
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# Импорт из файлов с хендлерами, роутеров
from handlers.credit_handlers import loan_credit_router
from handlers.common import common_router
from handlers.early_credit_handlers import loan_early_credit_router
from handlers.mortgage import loan_morgage_router

# Передача токена из телеграма боту
bot = Bot(token=os.getenv('TOKEN'))

# Подлючение всех роутеров к диспетчеру и вызов самого диспетчера
dp = Dispatcher()
dp.include_router(common_router)
dp.include_router(loan_credit_router)
dp.include_router(loan_early_credit_router)
dp.include_router(loan_morgage_router)

# Запуск бота через Polling, а так же удаление всех апдейтов
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
asyncio.run(main())

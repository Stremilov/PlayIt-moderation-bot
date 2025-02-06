from aiogram import types, Router
from aiogram.filters import Command

from src.core.utils.config import dp

start_router = Router()


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Сюда будут приходить задания на проверку. После проверки они будут удаляться")

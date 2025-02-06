import asyncio
import logging

from src.core.utils.config import settings, dp, bot
from src.handlers import main_router

logging.basicConfig(
    level=settings.logging.level,
    format=settings.logging.format,
)


async def main():
    try:
        logging.info("Запускаю бота...")
        dp.include_router(main_router)
        await dp.start_polling(bot)

    except Exception as ex:
        logging.error(f"Ошибка при запуске: {ex}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Работа завершена")

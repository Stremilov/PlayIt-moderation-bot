import logging

from aiogram import Bot, Dispatcher
from pydantic import BaseModel
from pydantic.v1 import BaseSettings

from dotenv import load_dotenv
import os


load_dotenv()

TOKEN = os.getenv("TOKEN", "")

bot = Bot(token=TOKEN)
dp = Dispatcher()


LOG_DEFAULT_FORMAT = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"


class LoggerConfig(BaseModel):
    level: int = logging.DEBUG
    format: str = LOG_DEFAULT_FORMAT


class Settings(BaseSettings):
    logging: LoggerConfig = LoggerConfig()


settings = Settings()

from aiogram import Router

from .callbacks.moderation import moderation_router
from .endpoints.start import start_router

main_router = Router()

main_router.include_routers(moderation_router, start_router)
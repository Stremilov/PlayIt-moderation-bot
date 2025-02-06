import requests
from aiogram import Router, F
from aiogram.types import CallbackQuery

API_URL = ""

moderation_router = Router()


@moderation_router.callback_query(F.data.startswith("approve_"))
async def process_department_choice(callback: CallbackQuery):
    task_id, user_id = callback.data.split(":")[1], callback.data.split(":")[2]

    response = requests.post(API_URL, json={"task_id": int(task_id), "status": "approved"})

    if response.status_code == 200:
        await callback.message.delete()
    else:
        await callback.answer("Ошибка при отправке данных", show_alert=True)


@moderation_router.callback_query(F.data.startswith("reject_"))
async def process_department_choice2(callback: CallbackQuery):
    task_id, user_id = callback.data.split(":")[1], callback.data.split(":")[2]

    response = requests.post(API_URL, json={"task_id": int(task_id), "status": "rejected"})

    if response.status_code == 200:
        await callback.message.delete()
    else:
        await callback.answer("Ошибка при отправке данных", show_alert=True)
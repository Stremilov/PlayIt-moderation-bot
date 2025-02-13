import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiohttp import ClientSession

moderation_router = Router()

API_URL = "http://localhost:8000/playit/auth/users/balance"


async def send_status_to_api(status: str, task_id: int, user_id: int, value: int = None):
    json_data = {
        "status": status,
        "task_id": task_id,
        "user_id": user_id
    }

    if value is not None:
        json_data["value"] = value

    async with ClientSession() as session:
        try:
            async with session.patch(API_URL, json=json_data) as response:
                print(response.status)
                print(await response.json())
                if response.status != 200:
                    error_text = await response.text()
                    logging.error(error_text)
                return True
        except Exception as e:
            print(e)
            logging.error(e)


@moderation_router.callback_query(F.data.startswith("approve_"))
async def process_department_choice(callback: CallbackQuery):
    task_id, user_id, value = map(int, callback.data.split("_")[1:4])
    print(task_id, user_id, value)
    result = await send_status_to_api("approved", task_id, user_id, value)
    print(result)
    if result:
        await callback.message.delete()
    else:
        await callback.answer("Ошибка при отправке данных", show_alert=True)


@moderation_router.callback_query(F.data.startswith("reject_"))
async def process_department_choice2(callback: CallbackQuery):
    task_id, user_id = map(int, callback.data.split("_")[1:3])

    if await send_status_to_api("rejected", task_id, user_id):
        await callback.message.delete()
    else:
        await callback.answer("Ошибка при отправке данных", show_alert=True)

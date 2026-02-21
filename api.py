import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL")
BOT_SECRET = os.getenv("BOT_SECRET")

# def telegram_auth(telegram_id, full_name):
#     response = requests.post(
#         f"{BASE_URL}/users/telegram-auth/",
#         json={
#             "telegram_id": telegram_id,
#             "full_name": full_name,
#         },
#         headers = {
#             "X-BOT-SECRET": BOT_SECRET,
#         }
#     )
#     return response.json()

def telegram_auth(telegram_id, full_name):
    response = requests.post(
        f"{BASE_URL}/users/telegram-auth/",
        json={
            "telegram_id": telegram_id,
            "full_name": full_name,
        },
        headers={
            "X-BOT-SECRET": BOT_SECRET
        }
    )

    if response.status_code != 200:
        raise Exception(f"Backend error: {response.status_code} - {response.text}")

    return response.json()

def get_products(token):
    response = requests.get(
        f"{BASE_URL}/products/",
        headers={
            "Authorization": f"Bearer {token}",
        }
    )
    return response.json()

import requests
from datetime import datetime
from telegram import Bot

# إعدادات البوت وتيليجرام
bot_token = "7094699436:AAF4x_wX7opS6dUeH6B9G4pAwNPH7eP7Vbc"
chat_id = "@marketeyeoptions"

# إعدادات العقد وPolygon
api_key = "Bw1qC9P9UvXhHDympuBEb3_JLE4_FW1F"
contract_symbol = "O:NVDA250516P00110000"
url = f"https://api.polygon.io/v3/snapshot/options/{contract_symbol}?apiKey={api_key}"

# جلب السعر الأخير للعقد
try:
    res = requests.get(url)
    data = res.json()

    last_price = data["results"]["last_quote"]["last"]["p"]
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"سعر NVDA 110 Put:\n{last_price} دولار\nالتوقيت: {time_now}"
except Exception as e:
    message = f"فشل في جلب السعر للعقد NVDA 110 Put\n{str(e)}"

# إرسال إلى تيليجرام
bot = Bot(token=bot_token)
bot.send_message(chat_id=chat_id, text=message)

import requests
from telegram import Bot

# إعدادات التيليجرام
TELEGRAM_TOKEN = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
CHAT_ID = '@marketeyeoptions'
bot = Bot(token=TELEGRAM_TOKEN)

# بيانات العقد
option_contract = 'O:NVDA250516P00110000'  # NVDA Put 110 - Exp: 2025-05-16
api_key = 'Bw1qC9P9UvXhHDympuBEb3_JLE4_FW1F'
url = f'https://api.polygon.io/v3/trades/options/{option_contract}?apiKey={api_key}'

# طلب البيانات
response = requests.get(url)
data = response.json()

try:
    trade = data['results'][0]
    price = trade['price']
    size = trade['size']
    timestamp = trade['sip_timestamp']

    message = f"""سعر عقد الأوبشن:
العقد: {option_contract}
السعر: {price}$
الكمية: {size}
"""
except Exception as e:
    message = f'فشل في جلب السعر: {str(e)}'

# إرسال النتيجة إلى تيليجرام
bot.send_message(chat_id=CHAT_ID, text=message)

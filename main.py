import requests
from telegram import Bot

TELEGRAM_BOT_TOKEN = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
TELEGRAM_CHANNEL_ID = '@marketeyeoptions'
POLYGON_API_KEY = '8X2aox8AI9r_jRp3t20tsFf56YW3pEy3'

option_contract = "O:NVDA250516P00110000"
polygon_url = f"https://api.polygon.io/v3/quotes/options/{option_contract}/last?apiKey={POLYGON_API_KEY}"

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    try:
        response = requests.get(polygon_url)
        text = response.text[:4000]  # تيليجرام لا يسمح برسائل أطول من 4096 حرف
        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=f"رد الخادم:\n{text}")
    except Exception as e:
        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=f"خطأ: {e}")

if __name__ == "__main__":
    main()

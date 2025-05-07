import requests
from telegram import Bot

# إعدادات تيليجرام
TELEGRAM_TOKEN = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
TELEGRAM_CHAT_ID = '@marketeyeoptions'

# إعدادات العقد من Polygon
POLYGON_API_KEY = '8X2aox8AI9r_jRp3t20tsFf56YW3pEy3'
OPTION_CONTRACT = 'O:NVDA250516P00110000'
POLYGON_URL = f'https://api.polygon.io/v3/snapshot/options/{OPTION_CONTRACT}?apiKey={POLYGON_API_KEY}'

# إرسال الرسالة إلى تليجرام
def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# جلب البيانات من Polygon
def fetch_option_data():
    try:
        response = requests.get(POLYGON_URL)
        if response.status_code != 200:
            send_telegram_message(f"رد الخادم: {response.status_code} page not found")
            return

        data = response.json()

        option = data.get("results", {})
        last_quote = option.get("last_quote", {})
        greeks = option.get("greeks", {})

        price = last_quote.get("ask", "N/A")
        volume = option.get("day", {}).get("volume", "N/A")
        open_interest = option.get("open_interest", "N/A")
        iv = greeks.get("iv", "N/A")

        msg = (
            "تحديث عقد أوبشن NVDA:\n"
            f"النوع: Put\n"
            f"السترايك: 110\n"
            f"الانتهاء: 2025-05-16\n"
            f"السعر (متأخر 15 د): {price}\n"
            f"الحجم: {volume}\n"
            f"الاهتمام المفتوح: {open_interest}\n"
            f"الض隐 الضمني (IV): {iv}\n"
            "#marketeye"
        )

        send_telegram_message(msg)

    except Exception as e:
        send_telegram_message(f"خطأ أثناء جلب البيانات:\n{str(e)}")

# تنفيذ الكود
fetch_option_data()

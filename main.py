import requests
import telegram

# --- إعدادات API و Telegram ---
api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
ticker = "O:NVDA250516P00110000"  # عقد بوت NVDA - سترايك 110 - ينتهي 2025-05-16
bot_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"

# --- جلب سعر العرض والطلب ---
def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    if "status" in data and data["status"] == "ERROR":
        return None, None, f"فشل في جلب البيانات: {data.get('error', 'غير معروف')}"

    try:
        quote = data["results"]["last_quote"]
        bid = quote.get("bid", "N/A")
        ask = quote.get("ask", "N/A")
        return bid, ask, None
    except Exception as e:
        return None, None, f"خطأ داخلي: {e}"

# --- إرسال إلى تيليجرام ---
def send_to_telegram(message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# --- تنفيذ الكود ---
bid, ask, error = get_option_price(ticker)

if error:
    send_to_telegram(f"فشل في جلب سعر عرض وطلب العقد:\n{ticker}\n{error}")
else:
    send_to_telegram(f"NVDA 110 Put - 2025-05-16\nسعر العرض: {bid}\nسعر الطلب: {ask}")

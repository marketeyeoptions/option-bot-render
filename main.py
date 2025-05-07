import requests
from telegram import Bot

# إعدادات
TELEGRAM_BOT_TOKEN = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
TELEGRAM_CHANNEL_ID = '@marketeyeoptions'
POLYGON_API_KEY = '8X2aox8AI9r_jRp3t20tsFf56YW3pEy3'

ticker = "NVDA"
target_contract = "NVDA250516P00110000"

polygon_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={POLYGON_API_KEY}"

def fetch_snapshot_price():
    try:
        response = requests.get(polygon_url)
        data = response.json()

        options = data.get("results", [])
        if not isinstance(options, list):
            return "خطأ: لم يتم العثور على بيانات الخيارات."

        # ابحث عن العقد داخل القائمة
        contract_data = next((item for item in options if item.get("details", {}).get("symbol") == target_contract), None)

        if not contract_data:
            return f"لم يتم العثور على العقد:\n{target_contract}"

        last_quote = contract_data.get("last_quote", {})
        greeks = contract_data.get("greeks", {})

        price = last_quote.get("midpoint", "N/A")
        bid = last_quote.get("bid", "N/A")
        ask = last_quote.get("ask", "N/A")
        delta = greeks.get("delta", "N/A")
        oi = contract_data.get("open_interest", "N/A")

        message = f"""تحديث عقد NVDA:
النوع: Put
السترايك: 110
الانتهاء: 2025-05-16
السعر (منتصف العرض/الطلب): {price}
العرض: {bid} | الطلب: {ask}
الـ Delta: {delta}
Open Interest: {oi}

#marketeye"""
        return message

    except Exception as e:
        return f"خطأ أثناء جلب البيانات:\n{e}"

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    message = fetch_snapshot_price()
    bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)

if __name__ == "__main__":
    main()

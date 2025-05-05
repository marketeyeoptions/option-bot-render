import requests
import telegram

# بيانات العقد
contract_id = "O:NVDA250516P00110000"
api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
bot_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"

# إرسال الرسالة
def send_to_telegram(message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# طلب البيانات من Polygon.io
try:
    url = f"https://api.polygon.io/v3/snapshot/options/{contract_id}?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    results = data.get("results", [])
    if isinstance(results, list) and len(results) > 0:
        option_data = results[0]
        ask = option_data.get("ask", "N/A")
        bid = option_data.get("bid", "N/A")
        greeks = option_data.get("greeks", {})
        delta = greeks.get("delta", "N/A")
        expiry = option_data.get("details", {}).get("expiration_date", "N/A")

        message = f"""NVDA 110 Put عقد
العرض: {bid}
الطلب: {ask}
الانتهاء: {expiry}
#عين_السوق"""
    else:
        message = f"فشل في جلب سعر عرض وطلب العقد:\n{contract_id}\n(النتائج فارغة)"

except Exception as e:
    message = f"فشل في جلب بيانات العقد:\n{contract_id}\nخطأ داخلي: {e}"

send_to_telegram(message)

import requests
import telegram

# إعدادات
polygon_api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
telegram_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"
option_id = "O:NVDA250516P00110000"

# رابط API
url = f"https://api.polygon.io/v3/reference/options/contracts/{option_id}?apiKey={polygon_api_key}"

try:
    response = requests.get(url)
    data = response.json()

    contract = data.get("results", {})
    if not contract:
        raise ValueError("العقد غير موجود أو لا يحتوي بيانات")

    strike_price = contract.get("strike_price", "N/A")
    expiration_date = contract.get("expiration_date", "N/A")
    contract_type = contract.get("contract_type", "N/A")
    ticker = contract.get("ticker", "N/A")

    message = (
        f"{ticker} عقد\n"
        f"النوع: {'Put' if contract_type == 'put' else 'Call'}\n"
        f"السترايك: {strike_price}\n"
        f"الانتهاء: {expiration_date}\n"
        f"#عين_السوق"
    )

except Exception as e:
    message = f"فشل في جلب بيانات العقد:\n{option_id}\nخطأ داخلي: {e}"

# إرسال إلى تيليجرام
bot = telegram.Bot(token=telegram_token)
bot.send_message(chat_id=chat_id, text=message)

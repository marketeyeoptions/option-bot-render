import requests
from telegram import Bot

# بيانات الاتصال
BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
CHAT_ID = "@marketeyeoptions"
API_KEY = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"

# رمز العقد (يبدأ بـ O:)
contract = "O:NVDA250516P00110000"

# رابط الاستعلام من Polygon
url = f"https://api.polygon.io/v3/reference/options/contracts/{contract}?apiKey={API_KEY}"

# تنفيذ الطلب
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # التعامل مع النتائج
    result = data.get("results", {})

    symbol = result.get("ticker", "N/A")
    underlying = result.get("underlying_ticker", "N/A")
    contract_type = result.get("contract_type", "N/A").capitalize()
    strike_price = result.get("strike_price", "N/A")
    expiration_date = result.get("expiration_date", "N/A")

    # تجهيز الرسالة
    message = f"""تحديث عقد أوبشن:
السهم: {underlying}
النوع: {contract_type}
السترايك: {strike_price}
الانتهاء: {expiration_date}
السعر: N/A (متأخر ١٥ د)
الحجم: N/A
الرمز: {symbol}
#marketeye"""

except Exception as e:
    message = f"خطأ أثناء جلب البيانات:\n{e}"

# إرسال النتيجة إلى تيليجرام
bot = Bot(token=BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text=message)

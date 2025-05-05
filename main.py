import requests
import telegram

# إعدادات
bot_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"
api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
option_contract = "O:NVDA250516P00110000"

# استعلام من بوليغون
url = f"https://api.polygon.io/v3/snapshot/options/{option_contract}?apiKey={api_key}"

try:
    response = requests.get(url)
    data = response.json()

    # نطبع الرد الكامل في اللوق للتحقق
    print("Raw Response from Polygon:")
    print(data)

    # إرسال تنبيه تجريبي لتيليجرام حتى نعرف أن الكود اشتغل
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text="تم طباعة الرد الكامل في اللوق. افحص Render.")

except Exception as e:
    print(f"Error: {e}")

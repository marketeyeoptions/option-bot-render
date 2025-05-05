import requests
import telegram

# إعدادات ثابتة
API_KEY = '8X2aox8AI9r_jRp3t20tsFf56YW3pEy3'
BOT_TOKEN = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
CHAT_ID = '@marketeyeoptions'
OPTION_CONTRACT = 'O:NVDA250516P00110000'

# الاتصال بـ Polygon API
url = f'https://api.polygon.io/v3/snapshot/options/{OPTION_CONTRACT}?apiKey={API_KEY}'
response = requests.get(url)
data = response.json()

# معالجة البيانات
try:
    option_data = data['results']
    ask = option_data['details']['ask']
    bid = option_data['details']['bid']
    last = option_data['details']['last']

    message = f"""عقد NVDA 110 Put  
العرض: {ask}  
الطلب: {bid}  
آخر سعر: {last}  
#عين_السوق"""

except Exception as e:
    message = f"فشل في جلب سعر عرض وطلب العقد:\n{OPTION_CONTRACT}\nخطأ داخلي: {e}"

# إرسال النتيجة إلى تليجرام
bot = telegram.Bot(token=BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text=message)

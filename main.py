import requests
import time
import telegram

# إعدادات
api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
telegram_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"

# بيانات العقد
option_contract = "O:NVDA250516P00110000"

# جلب بيانات العقد من Polygon
contract_url = f"https://api.polygon.io/v3/reference/options/contracts/{option_contract}?apiKey={api_key}"
contract_response = requests.get(contract_url)

if contract_response.status_code == 200:
    contract_data = contract_response.json()
    symbol = contract_data["results"]["underlying_ticker"]
    strike = contract_data["results"]["strike_price"]
    expiry = contract_data["results"]["expiration_date"]
    option_type = contract_data["results"]["contract_type"].capitalize()

    # جلب snapshot للأسعار
    snapshot_url = f"https://api.polygon.io/v3/snapshot/options/{option_contract}?apiKey={api_key}"
    snapshot_response = requests.get(snapshot_url)
    
    print("Snapshot Raw Response:")
    print(snapshot_response.text)  # <=== هذا يطبع النتيجة الخام لمراقبتها في Render

    if snapshot_response.status_code == 200:
        snapshot_data = snapshot_response.json()
        results = snapshot_data.get("results")

        if results:
            ask = results.get("ask", {}).get("price", "N/A")
            bid = results.get("bid", {}).get("price", "N/A")
            message = f"""عقد NVDA 110 Put
العرض: {bid}
الطلب: {ask}
الانتهاء: {expiry}
#عين_السوق"""
        else:
            message = f"فشل في جلب سعر عرض وطلب العقد:\n{option_contract}\n(النتائج فارغة)"
    else:
        message = f"فشل في جلب بيانات العقد:\n{option_contract}\n(status code {snapshot_response.status_code})"
else:
    message = f"فشل في جلب بيانات العقد:\n{option_contract}\n(status code {contract_response.status_code})"

# إرسال النتيجة إلى تليجرام
bot = telegram.Bot(token=telegram_token)
bot.send_message(chat_id=chat_id, text=message)

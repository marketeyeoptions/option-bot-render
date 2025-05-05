import requests

# إعدادات
bot_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"
polygon_api_key = "Bw1qC9PU9vXhHDympuBEb3_JLE4_FWlF"

# بيانات العقد
option_ticker = "O:NVDA250516P00110000"

# رابط API لجلب بيانات العقد
url = f"https://api.polygon.io/v3/snapshot/options/{option_ticker}?apiKey={polygon_api_key}"

try:
    response = requests.get(url)
    data = response.json()

    if "results" in data and data["results"]:
        option_data = data["results"]

        last_price = option_data["last_quote"]["p"] if "last_quote" in option_data else "N/A"
        bid = option_data["last_quote"]["bid"]
        ask = option_data["last_quote"]["ask"]

        message = f"سعر العقد الآن: {last_price}\nالعرض: {bid}\nالطلب: {ask}"
    else:
        message = f"فشل في جلب بيانات العقد {option_ticker}"

except Exception as e:
    message = f"حدث خطأ: {str(e)}"

# إرسال إلى تيليجرام
requests.post(
    f"https://api.telegram.org/bot{bot_token}/sendMessage",
    data={"chat_id": chat_id, "text": message}
)

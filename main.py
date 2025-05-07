import logging
import requests
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from PIL import Image
import pytesseract
from io import BytesIO

# إعدادات البوت
BOT_TOKEN = "7710712900:AAH8WFVY9GzhCjisF8CihBxW0onfLBN9LZQ"
CHANNEL_ID = "@marketeyeoptions"

# إعداد السجل
logging.basicConfig(level=logging.INFO)

# دالة استقبال الصورة
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    photo_bytes = await photo_file.download_as_bytearray()
    image = Image.open(BytesIO(photo_bytes))

    # استخراج النص من الصورة
    extracted_text = pytesseract.image_to_string(image)

    # محاولة استخلاص البيانات (بسيطة كبداية)
    symbol = "TSLA" if "TSLA" in extracted_text else "NVDA" if "NVDA" in extracted_text else "رمز غير معروف"
    option_type = "Call" if "C" in extracted_text or "call" in extracted_text.lower() else "Put" if "P" in extracted_text or "put" in extracted_text.lower() else "غير معروف"
    strike = next((word for word in extracted_text.split() if word.endswith("C") or word.endswith("P")), "غير محدد").strip("CP")
    expiry = "2025-05-16"  # مؤقتاً ثابت، يمكن تحسينه لاحقاً

    # إعداد التوصية
    message = f"""
توصية اليوم:  
السهم: ${symbol}  
النوع: شراء {option_type} {strike}  
الانتهاء: {expiry}  
الهدف:  
الستوب:  

#عين_السوق
    """

    # إرسالها إلى القناة
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHANNEL_ID, "text": message}
    )

# إعداد البوت
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

# تشغيل البوت
app.run_polling()

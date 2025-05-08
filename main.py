import logging
import requests
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from PIL import Image
import pytesseract
from io import BytesIO

# إعداد البوت
BOT_TOKEN = "7710712900:AAH8WFVY9GzhCjisF8cihBxW0nFLBN9LZQ"
CHANNEL_ID = "@marketeyeoptions"

logging.basicConfig(level=logging.INFO)

# دالة استقبال الصور
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    photo_bytes = await photo_file.download_as_bytearray()
    image = Image.open(BytesIO(photo_bytes))

    # استخراج النص من الصورة
    extracted_text = pytesseract.image_to_string(image)

    # استخراج البيانات من النص
    symbol = "TSLA" if "TSLA" in extracted_text else "NVDA" if "NVDA" in extracted_text else "رمز غير معروف"
    option_type = "Call" if "C" in extracted_text or "call" in extracted_text.lower() else "Put" if "P" in extracted_text else "نوع غير محدد"
    strike = next((word for word in extracted_text.split() if word.endswith("C") or word.endswith("P")), "غير محدد")
    expiry = "2025-05-16"  # يمكنك تحسين هذا لاحقاً من خلال تحليل التاريخ تلقائياً

    # تجهيز الرسالة
    message = f"""توصية جديدة:
السهم: {symbol}
النوع: {option_type}
الاسترايك: {strike}
الانتهاء: {expiry}

#عين_السوق"""

    # إرسال للقناة
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message)

# تشغيل البوت
if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.run_polling()

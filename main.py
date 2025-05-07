from telegram import Bot

TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
CHAT_ID = "@marketeyeoptions"
image_path = "nvda_put_110.png"

caption = "NVDA Put 110 – Exp: 2025-05-16\nPrice: 1.96 | Vol: 3.71k | OI: 2.23k | IV: 25%\n#marketeye"

bot = Bot(token=TOKEN)
with open(image_path, 'rb') as img:
    bot.send_photo(chat_id=CHAT_ID, photo=img, caption=caption)

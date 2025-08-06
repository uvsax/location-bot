from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7786101064:AAEHsY7be9Tk6SQtShnDR4jgmNxO59Qi2cQ"  # توكن البوت مالك
OWNER_CHAT_ID = 6028485445  # آيدي تيلي مالك

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = KeyboardButton("📍 إرسال موقعي", request_location=True)
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("اضغط الزر أدناه لإرسال موقعك:", reply_markup=keyboard)

async def location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = update.message.location
    if location:
        lat = location.latitude
        lon = location.longitude
        user_id = update.message.from_user.id
        await context.bot.send_message(
            chat_id=OWNER_CHAT_ID,
            text=f"📍 تم استلام موقع جديد من المستخدم {user_id}:\nLatitude: {lat}\nLongitude: {lon}"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.LOCATION, location_handler))
    print("البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    main()

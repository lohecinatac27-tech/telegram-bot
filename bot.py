from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "6463586992:AAGFsjXN5zFLMaIDs7IskkUkGUuq9Cmh6OU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is running 24/7.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

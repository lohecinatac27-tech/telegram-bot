from flask import Flask
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

BOT_TOKEN = "6463586992:AAGFsjXN5zFLMaIDs7IskkUkGUuq9Cmh6OU"
app = Flask(__name__)

def run_bot():
    asyncio.set_event_loop(asyncio.new_event_loop())
    
    bot_app = Application.builder().token(BOT_TOKEN).build()
    
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hello! Bot is running 24/7.")
    
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.run_polling()

threading.Thread(target=run_bot, daemon=True).start()

@app.route("/")
def home():
    return "Bot is alive!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
  

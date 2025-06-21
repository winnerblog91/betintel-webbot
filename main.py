from flask import Flask
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater, Dispatcher, CallbackContext
import os

# Initialisation Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Telegram Actif avec Flask sur Render"

# === Configuration du bot ===
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher: Dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🤖 Bot en ligne !")

dispatcher.add_handler(CommandHandler("start", start))

# Démarrage parallèle du bot
import threading

def run_bot():
    updater.start_polling()

threading.Thread(target=run_bot).start()

import logging
from telegram.ext import Updater,CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update
import warnings
warnings.filterwarnings('ignore')
from flask import Flask, request


#enable logging
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)

token = "1296395929:AAHg2AYv-i8DKTs-NTQXvZp7z_mQhNA1AZY"

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

@app.route(f'/{token}', methods = ['GET', 'POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)

    dp.process_update(update)
    return 'ok'


def start(bot, update):
    author = update.message.from_user.first_name
    reply = "Hi! {}".format(author)
    bot.send_message(chat_id=update.message.chat_id, text = reply)

def _help(bot, update):
    help_txt = "This is a help text"
    bot.send_message(chat_id = update.message.chat_id, text = reply)

def echo_text(bot, update):
    reply = update.message.text
    bot.send_message(chat_id = update.message.chat_id, text = reply)

def echo_sticker(bot, update):
    bot.send_sticker(chat_id = update.message.chat_id, 
        sticker = update.message.sticker.file_id)
    
def error(bot, update):
    logger.error("Update '%s' caused error '%s'", update, update.error)

   

if __name__ == "__main__":
   
    bot = Bot(token)
    bot.set_webhook("https://11b79e8742be.ngrok.io/" + token)
    dp = Dispatcher(bot, None)

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', _help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))

    app.run(port = 8443)

    
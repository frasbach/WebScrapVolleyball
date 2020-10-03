from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests, time


API_KEY = "1235547402:AAGH6JzzkZaR09uwBDtgRc-l9aqgOqmtga4"


print('Telegram Bot was read')
#TODO: Create bot functionality and co here and let it be called :)


def start(update, context):
  """Send a message when the command /start is issued."""
  update.message.reply_text('Hey I am going to inform you about new Cups posted on https://www.beachvolleyball.nrw/')

def help_command(update, context):
  """Send a message when the command /help is issued."""
  update.message.reply_text('Help-Function is not implemented yet!')

def send_message(message):
  print('Called send message()')
  url = f'https://api.telegram.org/bot{API_KEY}/sendMessage'
  data = {'chat_id': {-1001437326202}, 'text': message}
  requests.post(url, data).json()
  time.sleep(2)
  

def main():
  # Get the dispatcher to register handlers
  updater = Updater(API_KEY, use_context=True)
  dp = updater.dispatcher

  # on diffrent commands - answer in telegram
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", help_command))

  # Start the Bot
  updater.start_polling()
  #updater.idle()
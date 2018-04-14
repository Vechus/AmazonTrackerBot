import telebot
import logging
import simplejson

FEEDBACK = 12
logging.addLevelName(FEEDBACK, 'FEEDBACK')
logging.basicConfig(filename='testing.log', filemode='w+', level=logging.DEBUG)

bot = telebot.TeleBot("577135328:AAEBSQdPZE3UO4aUqt_pAWrrbBaGTST1DRM")

## Start / Help
@bot.message_handler(commands=['start','help'])
def sendWelcome(message):
    bot.reply_to(message, "Hello, this bot allows you to track an Amazon product price by name, url or category.")

@bot.message_handler(commands=['feedback'])
def sendFeedback(message):
    logging.log(FEEDBACK, "from: " + str(message.chat.username) + ": " + message.text)
    bot.reply_to(message, "Feedback sent!")


## Not implemented / not a command / bugged
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text + " is not a command.")

##### START BOT #####
bot.polling()

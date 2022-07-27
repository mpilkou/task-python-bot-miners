import telebot

import parser

from dotenv import dotenv_values

config = dotenv_values('variables')
SECRET_KEY = config['SECRET_KEY']

bot = telebot.TeleBot(SECRET_KEY)

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(commands = ['update'])
def update_message(message):

    miners_list = list(set(parser.get_miners_list()))
    miners_per_message = 100
    messages_number = len(miners_list) // miners_per_message

    for message_number in range(messages_number):
        miners_from = message_number * miners_per_message
        miners_to = miners_from + miners_per_message + 1
        bot.send_message(message.chat.id, '\n'.join(miners_list[miners_from: miners_to]))

    bot.send_message(message.chat.id, '\n'.join(miners_list[len(miners_list) % miners_per_message :]))



bot.polling()
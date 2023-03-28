import os
import telebot
import random

BOT_TOKEN = os.environ.get('BOT_TOKEN')
# bot = telebot.TeleBot('6274800702:AAFmqKG6LEnMLqqqJR75sxC17cbTjgdeohw')
bot = telebot.TeleBot('BOT_TOKEN')

options = ['rock', 'paper', 'scissors']

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Rock-Paper-Scissors! Type /play to start the game.")

@bot.message_handler(commands=['play'])
def play_game(message):
    bot.reply_to(message, "Choose your option: rock, paper or scissors.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_choice = message.text.lower()
    if user_choice not in options:
        bot.reply_to(message, "Invalid choice. Please choose either rock, paper or scissors.")
        return
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors' or \
            user_choice == 'paper' and computer_choice == 'rock' or \
            user_choice == 'scissors' and computer_choice == 'paper':
        result = "You win!"
    else:
        result = "Computer wins!"
    bot.reply_to(message, f"You chose {user_choice}, computer chose {computer_choice}. {result}")

bot.infinity_polling()
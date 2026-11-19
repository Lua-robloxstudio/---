
import telebot
import sqlite3
import config
from logic import create_database

bot = telebot.TeleBot(config.API_TOKEN)







@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Welcome to GameInfo!\n"
        "Use /help to see available commands."
    )



@bot.message_handler(commands=["help"])
def help_command(message):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title FROM games ORDER BY title")
    games = cursor.fetchall()

    conn.close()

    result = "COMMANDS:\n\n"
    result += "/help - Show commands and games\n"
    result += "/game_info NAME - Show game information\n\n"

    result += "GAMES:\n\n"

    for game in games:
        result += f"{game[0]}\n"

    bot.reply_to(message, result)


@bot.message_handler(commands=["game_info"])
def game_info(message):
    name = message.text.replace("/game_info", "", 1).strip()

    if not name:
        bot.reply_to(
            message,
            "Use: /game_info Minecraft"
        )
        return

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM games WHERE LOWER(title) = LOWER(?)",
        (name,)
    )

    game = cursor.fetchone()
    conn.close()

    if game:
        result = (
            f"Game: {game[1]}\n\n"
            f"Genre: {game[2]}\n"
            f"Multiplayer: {game[3]}\n"
            f"Platforms: {game[4]}\n"
            f"Release year: {game[5]}\n\n"
            f"Description: {game[6]}"
        )

        bot.reply_to(message, result)

    else:
        bot.reply_to(message, "Game not found in database.")


create_database()
bot.infinity_polling()

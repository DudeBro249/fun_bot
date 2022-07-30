from fun_bot.bot import FunBot
import discord
import fun_bot.constants as CONSTANTS


def main():
    bot = FunBot(command_prefix='$', intents=discord.Intents.all())
    bot.run(CONSTANTS.bot_token)


if __name__ == '__main__':
    main()

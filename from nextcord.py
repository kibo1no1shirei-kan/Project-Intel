from nextcord.ext import commands
from nextcord import *
import os
import nextcord
intents = nextcord.Intents.default()
intents.message_content = True

# the prefix is not used in this example
bot = commands.Bot(command_prefix='ho')







bot.run(os.environ["HMSBELFAST"])








import discord
from discord.ext import commands
import logging
import logging.handlers
import os
import asyncio

# Set Up Logging
log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logger = logging.getLogger('discord')
logging.getLogger('discord.http').setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    filename=os.path.join(log_dir, 'siberbot.log'),
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=50,             # Rotate through 50 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Set Up Bot
bot_token = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Load extensions
async def load_cogs():
    '''Activate cogs'''
    initial_extensions = []
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            extension = 'cogs.' + filename[:-3]
            print(f'Loading {extension}')
            initial_extensions.append(extension)
    for extension in initial_extensions:
        await bot.load_extension(extension)
asyncio.run(load_cogs())

# Ready event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Start bot
bot.run(bot_token, log_handler=handler, log_level=logging.DEBUG)
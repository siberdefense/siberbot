import discord
from discord.ext import commands

class Greetz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # commands
    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send("Ohaithere")

    # events
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Greetz ready')

async def setup(bot):
    await bot.add_cog(Greetz(bot))
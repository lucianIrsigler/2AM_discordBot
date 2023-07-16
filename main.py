from discord.ext import commands
from dotenv import load_dotenv
import os
import discord
import asyncio

initial_extensions = [f"cogs.{i.removesuffix('.py')}" for i in os.listdir("cogs") if "pycache" not in i]

# Loads the .env file
load_dotenv('config.env')


class Exception(Exception):
    pass
    """Raise for my specific kind of exception"""


# Intents
intentsBOT = discord.Intents.all()

bot = commands.Bot(command_prefix="$",
                   help_command=None, intents=intentsBOT)

bot.intents.members = True
bot.intents.message_content = True

class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.creator = 249901932548849664

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"Joined {guild.name}")
            

    @commands.Cog.listener()
    async def on_connect(self):
        for extension in initial_extensions:
            try:
                await bot.load_extension(extension)
                print(f"{extension} loaded")
            except Exception as e:
                print(e)

    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"Left {guild.name}")

    @commands.command()
    async def cogunload(self,ctx,cog):
        if cog in initial_extensions and ctx.author.id == self.creator:
            await bot.unload_extension(cog)
            await ctx.send(f"{cog} unloaded")
        else:
            await ctx.send("Invalid cog")

    @commands.command()
    async def cogload(self,ctx,cog):
        if cog in initial_extensions and ctx.author.id == self.creator:
            await bot.load_extension(cog)
            await ctx.send(f"{cog} loaded")
        else:
            await ctx.send("Invalid cog")

    @commands.command()
    async def cogreload(self,ctx,cog):
        if cog in initial_extensions and ctx.author.id == self.creator:       
            await bot.unload_extension(cog)
            await bot.load_extension(cog)
            await ctx.send(f"{cog} reloaded")
        else:
            await ctx.send("Invalid cog")

    @commands.command()
    async def cogs(self,ctx):
        if ctx.author.id == self.creator:
            await ctx.send(initial_extensions)

TOKEN = os.getenv("DISCORD_TOKEN")


async def main():
    async with bot:
        await bot.add_cog(Startup(bot))
        await bot.start(TOKEN)

asyncio.run(main())

import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pf = "$"

    @commands.group(invoke_without_command=True)
    async def help(self, ctx:commands.Context):
        """A custom help command

        Parameters
        _________
        None

        NB:
        a @commands.group() decorator is required to make this custom help command work.
        Basically it allows for subcommands(@helpfor.command()) to be called and invoked through
        $helpfor <command_name>, similar to how the default help command works.
        """

        # guild_prefix queries the database (main.GUILDS) to get the prefix for the guild
        em = discord.Embed(title="COMMANDS")
        em.add_field(name=f"Text commands", value=f"{self.pf}help text", inline=False)
        em.add_field(name=f"Music commands", value=f"{self.pf}help music", inline=False)
        await ctx.send(embed=em)


    @help.command()
    async def text(self, ctx:commands.Context):
        em = discord.Embed(title="Text")

        fields = {
            "gif":"Sends one random gif",
            "enable":"Enables spam command",
            "isEnabled":"Checks if spam command is enabled"
        }

        for i,j in fields.items():
            em.add_field(name=f"{self.pf}{i}", value=f"{j}", inline=False)

        await ctx.send(embed=em)

    @help.command()
    async def music(self, ctx:commands.Context):
        em = discord.Embed(title="Music")

        fields = {
            "play <link/name>":"plays a song.It accepts either links or an inputted name",
            "loop" :"loops current playing song", "shuffle" :"shuffles upcoming songs",
            "pause" :"pause current playback", "queue <song>" :"add a song to the queue",
            "stop" :"Bot stops playing music", "skip" :"skips the current song",
            "clear" :"clears the queue", "prev" :"plays the previous song",
            "resume" :"resumes the playback if paused",
            "songinfo" :"information about the song currently played",
            "history" :"lists the songs played by the bot in the current session",
            "volume <number>" :"sets volume of the bot"
        }

        for i,j in fields.items():
            em.add_field(name=f"{self.pf}{i}", value=f"{j}", inline=False)

        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))

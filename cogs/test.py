import discord

from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['c', 'cls', 'purge'])
    @has_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, amount: int = 1):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(embed=discord.Embed(description=f'** Deleted {amount} messages.**', color=0x0c0c0c),
                               delete_after=3)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.message.author.mention}!')

async def setup(bot):
    await bot.add_cog(Test(bot))
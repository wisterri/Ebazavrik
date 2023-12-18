import discord
import asyncio

import utilities.env

from discord.ext import commands
from settings import MODULES

# Load the environment variables.
env = utilities.env.load()

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(env.DISCORD_PREFIX),
    intents=discord.Intents.all(),
    help_command=None
)


async def main():
    setattr(bot, 'env', env)

    async with bot:
        for module in MODULES:
            await bot.load_extension('cogs.' + module)
            print(f'Loaded cogs.{module}')

        await bot.start(env.DISCORD_TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
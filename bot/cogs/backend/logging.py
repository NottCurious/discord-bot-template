from discord import Embed
from discord.ext.commands import Cog

from bot import constants
from bot.bot import Bot
from bot.log import get_logger
from bot.utils import scheduling

log = get_logger(__name__)


class Logging(Cog):
    """Debug logging module"""

    def __init__(self, bot: Bot):
        self.bot = bot

        scheduling.create_task(self.startup_greeting(), event_loop=self.bot.loop)

    async def startup_greeting(self) -> None:
        await self.bot.wait_until_guild_available()
        log.info("Bot Connected")

        embed = Embed(
            title="Connected!",
        )

        if not constants.DEBUG_MODE:
            try:
                await self.bot.get_channel(constants.Channels.bot_updates).send(
                    embed=embed
                )
            except:
                pass


def setup(bot: Bot) -> None:
    """Load the Logging cog."""
    bot.add_cog(Logging(bot))

import types

from discord.ext import commands

from fun_bot import exts
from fun_bot.exts import voice
from fun_bot.utils.extension import walk_extensions
from fun_bot.utils.voice import VoiceRoleAction, perform_voice_role_action


class FunBot(commands.Bot):
    async def setup_hook(self) -> None:
        await self.load_extensions(module=exts)


    async def on_ready(self) -> None:
        print(f'Logged in as {self.user}')

        # Add VC roles to everyone in a voice channel
        for guild in self.guilds:
            for voice_channel in guild.voice_channels:
                for member in voice_channel.members:
                    await perform_voice_role_action(
                        action=VoiceRoleAction.join,
                        voice_state=member.voice,
                        member=member,
                    )



    async def load_extensions(self, module: types.ModuleType) -> None:
        """
        Load all the extensions within the given module and save them to ``self.all_extensions``.
        This should be ran in a task on the event loop to avoid deadlocks caused by ``wait_for`` calls.
        """
        self.all_extensions = walk_extensions(module)

        for extension in self.all_extensions:
            await self.load_extension(extension)

import discord
from discord.ext import commands
from fun_bot.utils.voice import VoiceRoleAction, perform_voice_role_action


class VoiceCog(commands.Cog):
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel == None and after.channel != None:
            # User has joined vc
            await perform_voice_role_action(
                action=VoiceRoleAction.join,
                voice_state=after,
                member=member,
            )

        elif before.channel != None and after.channel == None:
            # User has left vc
            await perform_voice_role_action(
                action=VoiceRoleAction.leave,
                voice_state=before,
                member=member,
            )

        elif before.channel != None and after.channel != None and before.channel != after.channel:
            # User switched from one voice channel to another

            # If user moves from one voice channel to another,
            # it can be treated as two separate events:
            # 1. User leaves a voice channel
            # 2. User joins a different voice channel

            await perform_voice_role_action(
                action=VoiceRoleAction.leave,
                voice_state=before,
                member=member,
            )

            await perform_voice_role_action(
                action=VoiceRoleAction.join,
                voice_state=after,
                member=member,
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(VoiceCog(bot))

async def teardown(bot: commands.Bot):
    await bot.remove_cog('VoiceCog')

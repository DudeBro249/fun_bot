import enum

import discord


class VoiceRoleAction(enum.Enum):
    join = 1
    leave = 2

async def perform_voice_role_action(action: VoiceRoleAction, voice_state: discord.VoiceState, member: discord.Member):
    guild = voice_state.channel.guild

    # Get all roles with the same name as the voice channel
    roles = [role for role in guild.roles if role.name == voice_state.channel.name]

    if len(roles) == 0:
        # No roles found matching the name of the voice channel
        created_role = await guild.create_role(
            name=voice_state.channel.name
        )
        roles.append(created_role)

    # Use the first role found/created
    role = roles[0]

    if action == VoiceRoleAction.join:
        await member.add_roles(role)
    elif action == VoiceRoleAction.leave:
        await member.remove_roles(role)

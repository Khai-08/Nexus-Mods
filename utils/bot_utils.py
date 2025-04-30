import os, time

from discord.ext.commands import BucketType
from discord.ext import commands

from utils.config_utils import ConfigurationUtils

class BotFunctions:
    def __init__(self, bot):
        self.bot = bot
        self.global_settings = bot.global_settings

    def abbreviate_number(self, number):
        suffixes = ['', 'k', 'm', 'b', 't']
        suffix_index = 0
        
        while number >= 1000 and suffix_index < len(suffixes) - 1:
            number /= 1000
            suffix_index += 1

        return f"{number:.1f}{suffixes[suffix_index]}"

    def bypass_cooldown(self, ctx):
        if ctx.author.guild_permissions.administrator:
            return None
        else:
            return commands.CooldownMapping.from_cooldown(7, 60, BucketType.user).get_bucket(ctx)

    def capitalize_words(self, text):
        return ' '.join(word.capitalize() for word in text.split())

    def sync_commands(self, guild_id: int, command_name: str) -> bool:
        guild_id_str = str(guild_id)
        if guild_id_str not in self.global_settings:
            return False
        command_states = self.global_settings[guild_id_str].get("command_states", {})
        return command_states.get(command_name, False)
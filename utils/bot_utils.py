from discord.ext.commands import BucketType
from discord.ext import commands

class BotFunctions:
    def __init__(self, bot):
        self.bot = bot

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
import discord
from datetime import datetime
from discord import app_commands
from utils.api_utils import fetch_mod_by_game

def setup(bot):
    @bot.tree.command(name="search-mod", description="Displays information about a specific mod for a given game on Nexus Mods.")
    @app_commands.describe(game="Enter the game domain (e.g., skyrimspecialedition, fallout4, etc.)", mod_id="Enter the mod ID.")
    @bot.cmd_logger
    async def search_mod(interaction: discord.Interaction, game: str, mod_id: int):
        game = game.replace(" ", "").lower()
        try:
            mod_data = await fetch_mod_by_game(game, mod_id, bot.api_headers)
            if not mod_data:
                return await bot.error_embed(interaction, f"No `{mod_id}` found for `{game}`.")
            
            updatedTime, createdTime = mod_data.get("updated_time"), mod_data.get("created_time")
            updatedTimestamp = f"<t:{int(datetime.fromisoformat(updatedTime.replace('Z', '+00:00')).timestamp())}:R>" if updatedTime else "Unknown"
            createdTimestamp = f"<t:{int(datetime.fromisoformat(createdTime.replace('Z', '+00:00')).timestamp())}:D>" if updatedTime else "Unknown"
            summary = mod_data.get("summary", "No summary available.")
            max_length = 1024

            if len(summary) > max_length: summary = summary[:max_length] + "..." 

            embed = discord.Embed(description=f"### [{mod_data.get('name', 'Unknown Mod')}](https://www.nexusmods.com/{game}/mods/{mod_id}) \n**Summary**\n{summary}", color=bot.embed_color)
            embed.add_field(name="Version", value=mod_data.get("version", "v?.?.?"), inline=True)
            embed.add_field(name="Author", value=f"[{mod_data.get("author", "Unknown")}]({mod_data.get("uploaded_users_profile_url")})", inline=True)
            embed.add_field(name="Downloads", value=bot.bot_functions.abbreviate_number(mod_data.get("mod_downloads", 0)), inline=True)
            embed.add_field(name="Last Updated", value=updatedTimestamp, inline=True)
            embed.add_field(name="Created", value=createdTimestamp, inline=True)
            embed.set_footer(text=bot.footer_text, icon_url=bot.user.avatar.url)
            embed.set_thumbnail(url=mod_data.get("picture_url"))
            await interaction.response.send_message(embed=embed, ephemeral=False)

        except Exception as e:
            await bot.error_embed(interaction, f"An error occurred: {e}")
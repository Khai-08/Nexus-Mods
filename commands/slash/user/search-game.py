import discord
from discord import app_commands
from utils.api_utils import fetch_game

def setup(bot):
    @bot.tree.command(name="search-game", description="Displays information about a specific game on Nexus Mods.")
    @app_commands.describe(game="Enter the game domain (e.g., skyrimspecialedition, fallout4, etc.)")
    @bot.cmd_logger
    async def search_game(interaction: discord.Interaction, game: str):
        game = game.replace(" ", "").lower()
        try:
            game_data = await fetch_game(game, bot.api_headers)
            if not game_data:
                embed = discord.Embed(title=f"Game Not Found", description=f"No data found for game domain: `{game}`.", color=discord.Color.orange())
                embed.set_footer(text=bot.footer_text, icon_url=bot.user.avatar.url)
                return await interaction.response.send_message(embed=embed, ephemeral=False)

            embed = discord.Embed(description=f"### [{game_data.get("name", "Unknown Game")}](https://www.nexusmods.com/{game})", color=bot.embed_color)
            embed.add_field(name="Genre", value=game_data.get("genre", "N/A"), inline=True)
            categories = game_data.get("categories", [])
            if categories:
                cat_list = [cat.get("name", "Unnamed") for cat in categories][:3]
                formatted = ", ".join(cat_list)
                embed.add_field(name="Categories", value=f"{formatted} ({len(cat_list)})", inline=True)
            embed.add_field(name="Mods", value=bot.bot_functions.abbreviate_number(game_data.get("mods", 0)), inline=True)
            embed.add_field(name="Downloads", value=bot.bot_functions.abbreviate_number(game_data.get("downloads", 0)), inline=True)
            embed.add_field(name="File Count", value=bot.bot_functions.abbreviate_number(game_data.get("file_count", 0)), inline=True)
            embed.add_field(name="Endorsements", value=bot.bot_functions.abbreviate_number(game_data.get("file_endorsements", 0)), inline=True)
            embed.set_footer(text=bot.footer_text, icon_url=bot.user.avatar.url)
            await interaction.response.send_message(embed=embed, ephemeral=False)

        except Exception as e:
            await bot.error_embed(interaction, f"An error occurred: {e}")

import discord
from utils.api_utils import fetch_all_games

class GamesListPaginator(discord.ui.View):
    def __init__(self, bot, interaction, games, per_page=10):
        super().__init__()
        self.bot = bot
        self.interaction = interaction
        self.games = games
        self.per_page = per_page
        self.current_page = 0
        self.author_id = interaction.user.id
        self.total_pages = (len(games) - 1) // per_page + 1

        self.prev_button = discord.ui.Button(emoji="◀", style=discord.ButtonStyle.primary, disabled=True)
        self.next_button = discord.ui.Button(emoji="▶", style=discord.ButtonStyle.primary, disabled=self.total_pages <= 1)

        self.prev_button.callback = self.prev_page
        self.next_button.callback = self.next_page

        self.add_item(self.prev_button)
        self.add_item(self.next_button)

    def get_embed(self):
        start = self.current_page * self.per_page
        end = start + self.per_page
        games_page = self.games[start:end]

        embed = discord.Embed(title="All Nexus Mods Games", color=self.bot.embed_color)
        embed.set_footer(text=f"Page {self.current_page + 1} / {self.total_pages}", icon_url=self.bot.user.avatar.url)

        description = ""
        for idx, game in enumerate(games_page, start=self.current_page * self.per_page + 1):
            name = game.get("name", "Unknown")
            domain = game.get("domain_name", "N/A")
            game_id = game.get("id", "0")
            description += f"{idx}. [{name}](https://www.nexusmods.com/{domain}) (`ID: {game_id}`)\n"
        embed.description = description
        return embed

    async def update_buttons(self, interaction):
        self.prev_button.disabled = self.current_page == 0
        self.next_button.disabled = self.current_page >= self.total_pages - 1
        await interaction.response.edit_message(embed=self.get_embed(), view=self)

    async def prev_page(self, interaction: discord.Interaction):
        if interaction.user.id != self.author_id:
            return await interaction.response.send_message(embed=discord.Embed(description="You are not the author to perform this action.", color=discord.Color.red()), ephemeral=True)
        self.current_page -= 1
        await self.update_buttons(interaction)

    async def next_page(self, interaction: discord.Interaction):
        if interaction.user.id != self.author_id:
            return await interaction.response.send_message(embed=discord.Embed(description="You are not the author to perform this action.", color=discord.Color.red()), ephemeral=True)
        self.current_page += 1
        await self.update_buttons(interaction)

def setup(bot):
    @bot.tree.command(name="all-games", description="List all games available on Nexus Mods.")
    @bot.cmd_logger
    async def all_games(interaction: discord.Interaction):
        try:
            games = await fetch_all_games(bot.api_headers)
            if not games:
                embed = discord.Embed(title="No Games Found", description="Failed to fetch games from Nexus Mods.", color=bot.embed_color)
                embed.set_footer(text=bot.footer_text, icon_url=bot.user.avatar.url)
                return await interaction.response.send_message(embed=embed, ephemeral=False)

            view = GamesListPaginator(bot, interaction, games)
            await interaction.response.send_message(embed=view.get_embed(), view=view)

        except Exception as e:
            await bot.error_embed(interaction, f"An error occurred: {e}")
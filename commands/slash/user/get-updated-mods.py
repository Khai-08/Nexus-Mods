import discord
from discord import app_commands
from discord.ui import Button, View
from utils.api_utils import fetch_updated_mods

class UpdatedModsPaginator(View):
    def __init__(self, bot, interaction, mods, per_page=5):
        super().__init__()
        self.bot = bot
        self.interaction = interaction
        self.mods = [mod for mod in mods if mod.get("status") == "published"]
        self.per_page = per_page
        self.current_page = 0
        self.author_id = interaction.user.id
        self.total_pages = (len(self.mods) - 1) // per_page + 1

        self.prev_button = Button(emoji="◀", style=discord.ButtonStyle.primary, disabled=True)
        self.next_button = Button(emoji="▶", style=discord.ButtonStyle.primary, disabled=self.total_pages <= 1)

        self.prev_button.callback = self.prev_page
        self.next_button.callback = self.next_page

        self.add_item(self.prev_button)
        self.add_item(self.next_button)

    def get_embed(self):
        start = self.current_page * self.per_page
        end = start + self.per_page
        mods_page = self.mods[start:end]

        embed = discord.Embed(title=f"Latest Updated Mods", color=self.bot.embed_color)
        desc = ""
        for mod in mods_page:
            mod_id = mod.get("mod_id", 0)
            name = mod.get("name", "Unnamed Mod")
            summary = mod.get("summary", "No description provided.")
            link = f"[**{name}**](https://www.nexusmods.com/{self.bot.current_game}/mods/{mod_id})"
            desc += f"{link} \n> {summary[:150]}... \n\n"
        embed.description = desc.strip()
        embed.description = desc.strip()
        embed.add_field(name="\u200b", value=f"-# **Page {self.current_page + 1} / {self.total_pages}**", inline=False)
        embed.set_footer(text=self.bot.footer_text, icon_url=self.bot.user.avatar.url)
        embed.set_thumbnail(url="https://www.nexusmods.com/assets/images/nexus-logo.png")
        return embed

    async def update_buttons(self, interaction):
        self.total_pages = (len([mod for mod in self.mods if mod.get("status") == "published"]) - 1) // self.per_page + 1
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
    @bot.tree.command(name="updated-mods", description="Displays the top 10 latest updated mods from Nexus Mods.")
    @app_commands.describe(game="Enter the game domain (e.g., skyrimspecialedition, fallout4, etc.)")
    @bot.cmd_logger
    async def updated_mods(interaction: discord.Interaction, game: str):
        game = game.replace(" ", "").lower()
        try:
            mods = await fetch_updated_mods(game, bot.api_headers)
            if not mods:
                embed = discord.Embed(title=f"No Mods Found for {game}", description="No updated mods are currently available.", color=bot.embed_color)
                embed.set_footer(text=bot.footer_text, icon_url=bot.user.avatar.url)
                embed.set_thumbnail(url="https://www.nexusmods.com/assets/images/nexus-logo.png")
                return await interaction.response.send_message(embed=embed, ephemeral=False)

            bot.current_game = game
            if len(mods) > 5:
                view = UpdatedModsPaginator(bot, interaction, mods)
                await interaction.response.send_message(embed=view.get_embed(), view=view, ephemeral=False)

        except Exception as e:
            await bot.error_embed(interaction, f"An error occurred: {e}")
import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
import storage

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class AccountOrganiser(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)
    
    async def setup_hook(self):
        # Sync slash commands
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

bot = AccountOrganiser()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

def format_accounts(platform, accounts):
    if not accounts:
        return f"No accounts found for **{platform}**."
    
    response = f"**Accounts for {platform.capitalize()}**\n\n"
    for idx, acc in enumerate(accounts, 1):
        # Mobile copiable: use code blocks for username and password
        response += f"**Account {idx}:**\n"
        response += f"Username: `{acc['username']}`\n"
        response += f"Password: `{acc['password']}`\n\n"
    
    response += "*Tip: Long-press on the code blocks to copy on mobile.*"
    return response

@bot.tree.command(name="add", description="Add an account for a platform")
@app_commands.describe(
    platform="The platform (e.g. roblox, discord, steam)",
    username="The account username",
    password="The account password"
)
async def add(interaction: discord.Interaction, platform: str, username: str, password: str):
    # Store account details (ephemeral so only the user sees)
    storage.add_account(interaction.user.id, platform, username, password)
    await interaction.response.send_message(
        f"✅ Saved account for **{platform.lower()}**: `{username}`", 
        ephemeral=True
    )

@bot.tree.command(name="list", description="List all accounts for a specific platform")
@app_commands.describe(platform="The platform to list accounts for")
async def list_accounts(interaction: discord.Interaction, platform: str):
    accounts = storage.get_accounts(interaction.user.id, platform)
    await interaction.response.send_message(
        format_accounts(platform, accounts),
        ephemeral=True
    )

@bot.tree.command(name="roblox", description="Shortcut to list your Roblox accounts")
async def roblox(interaction: discord.Interaction):
    accounts = storage.get_accounts(interaction.user.id, "roblox")
    await interaction.response.send_message(
        format_accounts("roblox", accounts),
        ephemeral=True
    )

@bot.tree.command(name="platforms", description="List all platforms you have accounts for")
async def platforms(interaction: discord.Interaction):
    platforms_list = storage.get_platforms(interaction.user.id)
    if not platforms_list:
        await interaction.response.send_message("You haven't added any accounts yet!", ephemeral=True)
        return
    
    response = "**Your Platforms:**\n" + "\n".join([f"- {p.capitalize()}" for p in platforms_list])
    await interaction.response.send_message(response, ephemeral=True)

if __name__ == "__main__":
    if not TOKEN:
        print("Error: DISCORD_TOKEN not found in environment variables.")
    else:
        bot.run(TOKEN)

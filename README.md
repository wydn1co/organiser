# Discord Bot Organiser

A simple Discord bot to store and retrieve account information (like passwords) for various platforms.

## Features

- **Store Accounts**: Use `/add` to save account details for any platform (Roblox, Discord, Steam, etc.).
- **Retrieve Accounts**: Use `/list` or shortcuts like `/roblox` to view your stored accounts.
- **Mobile Friendly**: Passwords and usernames are formatted in code blocks for easy copying on mobile.
- **Privacy First**: All account details are sent as **ephemeral messages**, meaning only you can see them.

## Commands

- `/add [platform] [username] [password]`: Save an account.
- `/list [platform]`: List all accounts for a platform.
- `/roblox`: Shortcut to list your Roblox accounts.
- `/platforms`: List all platforms you have accounts for.

## Setup

1. **Install Python**: Make sure you have Python 3.8+ installed.
2. **Install Dependencies**:
   ```bash
   pip install discord.py python-dotenv
   ```
3. **Configure the Bot**:
   - Create a new bot application in the [Discord Developer Portal](https://discord.com/developers/applications).
   - Get your bot's **Token**.
   - Copy the token into the `.env` file:
     ```env
     DISCORD_TOKEN=your_bot_token_here
     ```
4. **Invite the Bot**:
   - In the Developer Portal, go to **OAuth2** -> **URL Generator**.
   - Select `bot` and `applications.commands` scopes.
   - For bot permissions, select `Send Messages` and `Use Slash Commands`.
   - Copy the generated URL and use it to invite the bot to your server.
5. **Run the Bot**:
   ```bash
   python bot.py
   ```

## Security Note

This bot stores passwords in a local `accounts.json` file in plain text. For production use or sharing sensitive data, consider implementing encryption or using a secure database.

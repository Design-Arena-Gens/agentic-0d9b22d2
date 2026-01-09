# Discord Bot

A feature-rich Discord bot built with Python and discord.py.

## Features

- **Ping Command** (`!ping`) - Check bot latency
- **Hello Command** (`!hello`) - Get a friendly greeting
- **Info Command** (`!info`) - Display bot information
- **Roll Command** (`!roll [sides]`) - Roll a dice with custom sides (default 6)
- **Clear Command** (`!clear [amount]`) - Clear messages (requires manage messages permission)
- **User Info Command** (`!userinfo [@user]`) - Get detailed information about a user

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create Discord Bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the "Bot" section and create a bot
   - Copy the bot token
   - Enable the following Privileged Gateway Intents:
     - Message Content Intent
     - Server Members Intent

3. **Configure Environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_actual_bot_token_here
   ```

4. **Invite Bot to Server**
   - Go to OAuth2 > URL Generator
   - Select scopes: `bot`
   - Select permissions:
     - Read Messages/View Channels
     - Send Messages
     - Manage Messages
     - Embed Links
     - Read Message History
   - Copy the generated URL and open it in your browser to invite the bot

5. **Run the Bot**
   ```bash
   python bot.py
   ```

## Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `!ping` | Check bot latency | `!ping` |
| `!hello` | Get a greeting | `!hello` |
| `!info` | Display bot info | `!info` |
| `!roll` | Roll a dice | `!roll` or `!roll 20` |
| `!clear` | Clear messages | `!clear` or `!clear 10` |
| `!userinfo` | Get user info | `!userinfo` or `!userinfo @user` |

## Requirements

- Python 3.8+
- discord.py 2.3.2+
- python-dotenv

## Note

This bot is designed to run locally or on a server. Discord bots require a persistent connection and cannot be deployed to serverless platforms like Vercel.

For production deployment, consider:
- VPS (DigitalOcean, Linode, AWS EC2)
- Dedicated bot hosting (Heroku, Railway, Render)
- Docker containers

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.command(name='ping', help='Check bot latency')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')

@bot.command(name='hello', help='Say hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

@bot.command(name='info', help='Get bot information')
async def info(ctx):
    embed = discord.Embed(
        title="Bot Information",
        description="A simple Discord bot built with Python",
        color=discord.Color.blue()
    )
    embed.add_field(name="Servers", value=len(bot.guilds), inline=True)
    embed.add_field(name="Users", value=len(bot.users), inline=True)
    embed.add_field(name="Prefix", value="!", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='roll', help='Roll a dice (default 6-sided)')
async def roll(ctx, sides: int = 6):
    import random
    if sides < 2:
        await ctx.send("Dice must have at least 2 sides!")
        return
    if sides > 1000:
        await ctx.send("That's too many sides!")
        return
    result = random.randint(1, sides)
    await ctx.send(f'🎲 You rolled a {result} (d{sides})')

@bot.command(name='clear', help='Clear messages (requires manage messages permission)')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    if amount < 1:
        await ctx.send("Amount must be at least 1!")
        return
    if amount > 100:
        await ctx.send("Cannot delete more than 100 messages at once!")
        return
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f'Cleared {amount} messages!')
    await msg.delete(delay=3)

@bot.command(name='userinfo', help='Get information about a user')
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(
        title=f"User Info - {member}",
        color=member.color
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Nickname", value=member.nick or "None", inline=True)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Roles", value=len(member.roles) - 1, inline=True)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Missing argument: {error.param.name}')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command!')
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        await ctx.send(f'An error occurred: {str(error)}')

if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("ERROR: DISCORD_TOKEN not found in environment variables!")
        print("Please set your Discord bot token in the .env file")
        exit(1)
    bot.run(token)

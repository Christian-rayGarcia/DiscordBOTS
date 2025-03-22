import discord
import datetime
import random
from discord.ext import tasks, commands
import os
from dotenv import load_dotenv
from motivational_quotes import motivational_quotes  # Import the quotes array

# Replace with your bot token
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Replace with your actual channel ID
CHANNEL_ID = 

# Replace with your logging channel ID
LOG_CHANNEL_ID =

intents = discord.Intents.default()
intents.reactions = True  # Enable reaction tracking
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    post_date.start()


@tasks.loop(time=datetime.time(hour=5, minute=0))  # Runs daily at 5 AM
async def post_date():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        quote = random.choice(motivational_quotes)
        message = await channel.send(f"**Good morning!** Today's date: **{today}** {quote}")
        bot.last_message_id = message.id  # Store message ID for tracking reactions


@bot.event
async def on_reaction_add(reaction, user):
    """ Tracks when a user reacts with ✅ """
    if reaction.message.id == getattr(bot, "last_message_id", None) and str(reaction.emoji) == "✅":
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{user.name} checked in at {timestamp}")

        # Log the data in another channel
        log_channel = bot.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            await log_channel.send(f"✅ {user.mention} checked in at **{timestamp}**.")


bot.run(TOKEN)
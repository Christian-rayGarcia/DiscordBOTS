import discord
import datetime
from discord.ext import tasks, commands

# Replace with your bot token
TOKEN = "Your token here"

# Replace with your actual channel ID
CHANNEL_ID = YOUR_CHANNEL_ID

intents = discord.Intents.default()
intents.reactions = True  # Enable reaction tracking
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    post_date.start()


@tasks.loop(time=datetime.time(hour=5, minute=0)) # Runs daily at 5 AM
async def post_date():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        message = await channel.send(f"**Good morning!** Today's date: **{today}** A new day, a fresh start, Show up, "
                                     f"put in the work, and stack those smalls wins!")
        bot.last_message_id = message.id  # Store message ID for tracking reactions


@bot.event
async def on_reaction_add(reaction, user):
    """ Tracks when a user reacts with ✅ """
    if reaction.message.id == getattr(bot, "last_message_id", None) and str(reaction.emoji) == "✅":
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{user.name} checked in at {timestamp}")

        # Log the data in another channel
        log_channel = bot.get_channel(YOUR CHANNEL ID HERE)
        if log_channel:
            await log_channel.send(f"✅ {user.mention} checked in at **{timestamp}**.")


bot.run(TOKEN)

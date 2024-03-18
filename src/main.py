import interactions
import re
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

bot = interactions.Client(token=os.getenv('token'))

@interactions.slash_command(
    name="profanitychannel",
    description="Get profanity in current channel"
)
async def profanitychannel(ctx):
    profanityCount = 0
    for message in await ctx.channel.history(limit=1000).flatten():
        profanityCount += sum((message.content.lower().count(profanity) for profanity in ("fuck", "arse", "ass", "cock", "bitch", "bloody", "blowjob", "bugger", "bullshit", "shit", "damn", "dick", "prick", "pussy", "shit", "hell", "slut", "twat", "wanker", "whore")))
    
    await ctx.send(f"Watch your language! You have used profanity `{profanityCount}` times in this channel.")

@interactions.slash_command(
    name="profanityuser",
    description="Get profanity of user in server",
    options=[
        {
            "name": "user",
            "description": "Username of users' who profanity usage you would like to view",
            "type": interactions.OptionType.USER,
            "required": True
        }
    ]
)
async def profanityuser(ctx, user: interactions.Member):
    profanityCount = 0
    for message in [message for message in await ctx.channel.history(limit=1000).flatten() if message.author.id == user.id]:
        profanityCount += sum((message.content.lower().count(profanity) for profanity in ("fuck", "arse", "ass", "cock", "bitch", "bloody", "blowjob", "bugger", "bullshit", "shit", "damn", "dick", "prick", "pussy", "shit", "hell", "slut", "twat", "wanker", "whore")))
    
    await ctx.send(f"Watch your language! {user.mention} has used profanity `{profanityCount}` times in this channel.")

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

bot.start()

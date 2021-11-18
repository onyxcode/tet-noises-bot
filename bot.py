import discord
import json
import jishaku
from credentials import Token
from discord import commands
import discord.ext.commands


client = discord.ext.commands.AutoShardedBot(command_prefix="ts!")

@client.event
async def on_ready():
    print(f'{client.user} now online.')

client.remove_command("help")
client.load_extension("jishaku")

@client.command()
async def noise(ctx, supplied_noise_id: str = None):
    f = open("noise_ids.json")
    ids = json.load(f)
    if supplied_noise_id in ids:
        await ctx.send(file=discord.File(filename=ids[supplied_noise_id], fp=f"noises/{ids[supplied_noise_id]}"), content=f"Here is Tet noise `{supplied_noise_id}`.")
    else:
        await ctx.send("Tet noise not found. Please check your spelling and capitalization.")

@client.command()
async def help(ctx):
    await ctx.send("All IDs can be found here:\n> https://onyxcode.github.io/tet-noises-help/")

@client.command()
async def invite(ctx):
    await ctx.send("Invite this bot to your server :smiley:\n> https://discord.com/oauth2/authorize?client_id=902763473879068692&scope=bot&permissions=2147781632")

client.run(Token.token)

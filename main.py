import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

pveDamage = https://discord.com/channels/432275331794206720/1229880149525266523/1229880149525266523

@tree.command(
    name="pvedamage",
    description="A link to PvE Damage thread",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For more help with PvE Damage please see {pveDamage}")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=432275331794206720))
    print("Ready!")

client.run("MTIzNDMwOTA1MDMyNjU4MTI4OQ.GyprOE.ZyHC5oBXijU07-rk0BHR5eGIDhjJsgDsHK-_pY")
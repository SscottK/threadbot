import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

pveDamage = "https://discord.com/channels/432275331794206720/1229880149525266523/1229880149525266523"
destiny_utilities = "https://discord.com/channels/432275331794206720/1229090839129489449"
mvmnttech = "https://discord.com/channels/432275331794206720/1229882756700311663"
pvputilities = "https://discord.com/channels/432275331794206720/1229878291071242351"
warlordsruin = "https://discord.com/channels/432275331794206720/1229304195325235220"
GotD = "https://discord.com/channels/432275331794206720/1229154661261377587"
spire = "https://discord.com/channels/432275331794206720/1229151686497665214"
RoN = "https://discord.com/channels/432275331794206720/1229148398381174884"
grasp = "https://discord.com/channels/432275331794206720/1229146115367243817"
duality = "https://discord.com/channels/432275331794206720/1229144486450429963"
prophecy = "https://discord.com/channels/432275331794206720/1229143133430878209"
pit = "https://discord.com/channels/432275331794206720/1229141163051847803"
lastwish = "https://discord.com/channels/432275331794206720/1229139443160453271"
shatteredthrone = "https://discord.com/channels/432275331794206720/1229135680190287982"
crota = "https://discord.com/channels/432275331794206720/1229128539240927313"
vow = "https://discord.com/channels/432275331794206720/1229125200780595290"
kingsfall = "https://discord.com/channels/432275331794206720/1229118195882000404"
dsc = "https://discord.com/channels/432275331794206720/1229111831159898284"
vog = "https://discord.com/channels/432275331794206720/1229104380226179134"
garden = "https://discord.com/channels/432275331794206720/1229100329539473519"



@tree.command(
    name="pvedamage",
    description="A link to PvE Damage thread",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For more help with PvE Damage please see {pveDamage}")

@tree.command(
    name="destiny-utilities",
    description="A link to destiny-ustilities",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"If you need help on your journey please see {destiny_utilities} for information ranging from Damage metas to encounter and activity guides.")

@tree.command(
    name="Movement Tec",
    description="A link to guides on Movement Tec",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For more information on the best Movement Tec please see {mvmnttech}")

@tree.command(
    name="PvP Utilities",
    description="A link to all things PvP",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For the latest PvP metas check out {pvputilities}")

@tree.command(
    name="Warlards Ruin",
    description="A link to Warlords Ruin guides",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Warlords Ruin please see{warlordsruin}")

@tree.command(
    name="Ghosts of the Deep",
    description="A link to guides for Ghosts of the Deep dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Ghosts of the Deep dungeon please see{GotD}")

@tree.command(
    name="Spire of the Watcher",
    description="A linkg to guides for Spire of the Watcher dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Spire of the Watcher please see{spire}")

@tree.command(
    name="Root of Nightmares",
    description="A link to guides for Root of Nightmares",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Root of Nightmares please see {RoN}")

@tree.command(
    name="Grasp of Avarice",
    description="A link to guides for Grasp of Avaraice dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Grasp of Avarice dungeon please see {grasp}")

@tree.command(
    name="Duality",
    description="A link to guides for Duality dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Duality dungeon please see {duality}")

@tree.command(
    name="Prophecy",
    description="A link to guides for Prophecy dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Prophecy dungeon please see{prophecy}")

@tree.command(
    name="Pit of Heresy",
    description="A link to guides for Pit of Heresy dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Pit of Heresy dungeon please see{pit}")

@tree.command(
    name="Last Wish",
    description="A link to guides for Last Wish raid",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Last Wish raid please see {lastwish}")

@tree.command(
    name="Shattered Throne",
    description="A link to guides for Shattered Throne dungeon ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Shattered throne please see {shatteredthrone}")

@tree.command(
    name="Crota's End",
    description="A link to guides for Crota's End raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Crota's End raid please see {crota}")

@tree.command(
    name="Vow of the Disciple",
    description="A link to guides for Vow of the Disciple raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Vow of the Disciple raid please see {vow}")

@tree.command(
    name="Kingsfall",
    description="A link to guides for Kingsfall raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Kingsfall raid please see {kingsfall}")

@tree.command(
    name="Deep Stone Crypt",
    description="A link to guides for Deep Stone Crypt raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Deep Stone Crypt raid please see {dsc}")

@tree.command(
    name="Vault of Glass",
    description="A link to guides for Vault of Glass raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Vault of Glass raid please see {vog}")

@tree.command(
    name="Garden of Salvation",
    description="A link to guides for Garden of Salvation raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    await interaction.response.send_message(f"For help with Garden of Salvation raid please see {garden}")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=432275331794206720))
    print("Ready!")

client.run("MTIzNDMwOTA1MDMyNjU4MTI4OQ.GyprOE.ZyHC5oBXijU07-rk0BHR5eGIDhjJsgDsHK-_pY")
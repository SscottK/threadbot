import discord
from discord import app_commands

import os
from dotenv import load_dotenv, find_dotenv



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

channel_list = [432275331794206722, 685293052314517530]

@tree.command(
    name="pve_damage",
    description="A link to PvE Damage thread",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For more help with PvE Damage please see {pveDamage}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)

@tree.command(
    name="destiny-utilities",
    description="A link to destiny-ustilities",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"If you need help on your journey please see {destiny_utilities} for information ranging from Damage metas to encounter and activity guides.")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)

@tree.command(
    name="movement_tec",
    description="A link to guides on Movement Tec",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For more information on the best Movement Tec please see {mvmnttech}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)

@tree.command(
    name="pvp_utilities",
    description="A link to all things PvP",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For the latest PvP metas check out {pvputilities}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="warlards_ruin",
    description="A link to Warlords Ruin guides",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Warlords Ruin please see{warlordsruin}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="ghosts_of_the_deep",
    description="A link to guides for Ghosts of the Deep dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Ghosts of the Deep dungeon please see{GotD}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="spire_of_the_watcher",
    description="A linkg to guides for Spire of the Watcher dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Spire of the Watcher please see{spire}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="root_of_nightmares",
    description="A link to guides for Root of Nightmares",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Root of Nightmares please see {RoN}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="grasp_of_avarice",
    description="A link to guides for Grasp of Avaraice dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Grasp of Avarice dungeon please see {grasp}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="duality",
    description="A link to guides for Duality dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Duality dungeon please see {duality}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="prophecy",
    description="A link to guides for Prophecy dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Prophecy dungeon please see{prophecy}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="pit_of_heresy",
    description="A link to guides for Pit of Heresy dungeon",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Pit of Heresy dungeon please see{pit}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="last_wish",
    description="A link to guides for Last Wish raid",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Last Wish raid please see {lastwish}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="shattered_throne",
    description="A link to guides for Shattered Throne dungeon ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Shattered throne please see {shatteredthrone}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="crotas_end",
    description="A link to guides for Crota's End raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Crota's End raid please see {crota}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="vow_of_the_disciple",
    description="A link to guides for Vow of the Disciple raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Vow of the Disciple raid please see {vow}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="kingsfall",
    description="A link to guides for Kingsfall raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Kingsfall raid please see {kingsfall}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="deep_stone_crypt",
    description="A link to guides for Deep Stone Crypt raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Deep Stone Crypt raid please see {dsc}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="vault_of_glass",
    description="A link to guides for Vault of Glass raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Vault of Glass raid please see {vog}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@tree.command(
    name="garden_of_salvation",
    description="A link to guides for Garden of Salvation raid ",
    guild=discord.Object(id=432275331794206720)
)
async def pveDamage_command(interaction):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(f"For help with Garden of Salvation raid please see {garden}")
    else:
        await interaction.response.send_message("You can't use this command in this channel", ephemeral=True)
    
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=432275331794206720))
    print("Ready!")
    
    
load_dotenv(find_dotenv())
client.run(os.environ.get("TOKEN"))
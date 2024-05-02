import discord
from discord import app_commands

import os
from dotenv import load_dotenv, find_dotenv



intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

links = {
    "pveDamage" : "https://discord.com/channels/432275331794206720/1229880149525266523/1229880149525266523",
    "destiny_utilities" : "https://discord.com/channels/432275331794206720/1229090839129489449",
    "mvmnttech" : "https://discord.com/channels/432275331794206720/1229882756700311663",
    "pvputilities" : "https://discord.com/channels/432275331794206720/1229878291071242351",
    "warlordsruin" : "https://discord.com/channels/432275331794206720/1229304195325235220",
    "GotD" : "https://discord.com/channels/432275331794206720/1229154661261377587",
    "spire" : "https://discord.com/channels/432275331794206720/1229151686497665214",
    "RoN" : "https://discord.com/channels/432275331794206720/1229148398381174884",
    "grasp" : "https://discord.com/channels/432275331794206720/1229146115367243817",
    "duality" : "https://discord.com/channels/432275331794206720/1229144486450429963",
    "prophecy" : "https://discord.com/channels/432275331794206720/1229143133430878209",
    "pit" : "https://discord.com/channels/432275331794206720/1229141163051847803",
    "lastwish" : "https://discord.com/channels/432275331794206720/1229139443160453271",
    "shatteredthrone" : "https://discord.com/channels/432275331794206720/1229135680190287982",
    "crota" : "https://discord.com/channels/432275331794206720/1229128539240927313",
    "vow" : "https://discord.com/channels/432275331794206720/1229125200780595290",
    "kingsfall" : "https://discord.com/channels/432275331794206720/1229118195882000404",
    "dsc" : "https://discord.com/channels/432275331794206720/1229111831159898284",
    "vog" : "https://discord.com/channels/432275331794206720/1229104380226179134",
    "garden" : "https://discord.com/channels/432275331794206720/1229100329539473519"
}

messages = {
    "pveDamage" : f"For more help with PvE Damage please see {links["pveDamage"]}",
    "destiny_utilities" : f"If you need help on your journey please see {links["destiny_utilities"]} for information ranging from Damage metas to encounter and activity guides.",
    "mvmnttech" : f"For more information on the best Movement Tec please see {links["mvmnttech"]}",
    "pvputilities" : f"For the latest PvP metas check out {links["pvputilities"]}",
    "warlordsruin" : f"For help with Warlords Ruin please see {links["warlordsruin"]}",
    "GotD" : f"For help with Ghosts of the Deep dungeon please see {links["GotD"]}",
    "spire" : f"For help with Spire of the Watcher please see {links["spire"]}",
    "RoN" : f"For help with Root of Nightmares please see {links["RoN"]}",
    "grasp" : f"For help with Grasp of Avarice dungeon please see {links["grasp"]}",
    "duality" : f"For help with Duality dungeon please see {links["duality"]}",
    "prophecy" : f"For help with Prophecy dungeon please see {links["prophecy"]}",
    "pit" : f"For help with Pit of Heresy dungeon please see {links["pit"]}",
    "lastwish" : f"For help with Last Wish raid please see {links["lastwish"]}",
    "shatteredthrone" : f"For help with Shattered throne please see {links["shatteredthrone"]}",
    "crota" : f"For help with Crota's End raid please see {links["crota"]}",
    "vow" : f"For help with Vow of the Disciple raid please see {links["vow"]}",
    "kingsfall" : f"For help with Kingsfall raid please see {links["kingsfall"]}",
    "dsc" : f"For help with Deep Stone Crypt raid please see {links["dsc"]}",
    "vog" : f"For help with Vault of Glass raid please see {links["vog"]}",
    "garden" : f"For help with Garden of Salvation raid please see {links["garden"]}"
}

channel_list = [432275331794206722, 685293052314517530]

@tree.command(
    name = "link",
    description = "Return link to destiny-utilities thread",
    guild=discord.Object(id=432275331794206720))
@app_commands.choices(activity = [
    app_commands.Choice(name="PVE Damage", value= "pveDamage" ),
    app_commands.Choice(name="Destiny Utilities", value= "destiny_utilities" ),
    app_commands.Choice(name="Movement Tech", value= "mvmnttech" ),
    app_commands.Choice(name="PVP Utilities", value= "pvputilities" ),
    app_commands.Choice(name="Warlord's Ruin", value= "warlordsruin" ),
    app_commands.Choice(name="Ghosts of the Deep", value= "GotD" ),
    app_commands.Choice(name="Spire of the Watcher", value= "spire" ),
    app_commands.Choice(name="Root of Nightmares", value= "RoN" ),
    app_commands.Choice(name="Grasp of Avarice", value= "grasp" ),
    app_commands.Choice(name="Duality", value= "duality" ),
    app_commands.Choice(name="Prophecy", value= "prophecy" ),
    app_commands.Choice(name="Pit of Heresy", value= "pit" ),
    app_commands.Choice(name="Last Wish", value= "lastwish" ),
    app_commands.Choice(name="Shattered Throne", value= "shatteredthrone" ),
    app_commands.Choice(name="Crota's End", value= "crota" ),
    app_commands.Choice(name="Vow of the Disciple", value= "vow" ),
    app_commands.Choice(name="King's Fall", value= "kingsfall" ),
    app_commands.Choice(name="Deep Stone Crypt", value= "dsc" ),
    app_commands.Choice(name="Vault of Glass", value= "vog" ),
    app_commands.Choice(name="Garden of Salvation", value= "garden" )])
async def link_command(interaction, activity):
    if interaction.channel.id in channel_list:
        await interaction.response.send_message(messages[activity])
    else:
        await interaction.response.send_message("You can't use this command in this channel.", ephemeral=True)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=432275331794206720))
    print("Ready!")    

load_dotenv(find_dotenv())
client.run(os.environ.get("TOKEN"))
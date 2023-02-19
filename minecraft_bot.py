import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os
from asyncio import sleep
from mcstatus import JavaServer


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot()

globe_emoji = '🌐'
x_emoji = '❌'
people_emoji = '👥'
channel_id = 1076687011827683358
#server_ip = "localhost"
server_ip = str(os.getenv('MINECRAFT_IP'))

@bot.event
async def on_ready():
    await server_status_loop()


async def server_status_loop():
    while True:
        server = JavaServer.lookup(server_ip)
        try:
            status = server.status()
            online = True
        except:
            online = False

        channel = bot.get_channel(channel_id)
        if online:
            await channel.edit(name="Minecraft: " + globe_emoji + ' | ' + str(status.players.online) + people_emoji)
        else:
            await channel.edit(name="Minecraft: " + x_emoji)

        await sleep(60)


# @bot.slash_command(name='status', description='Minecraft server status')
# async def status(ctx):
#     server = JavaServer.lookup(server_ip)
#     try:
#         status = server.status()
#         online = True
#     except:
#         online = False
#     if online:
#         num_players = status.players.online
#         minecraft_str = f"The server has {num_players} player(s) online."
#         query = server.query()
#         if num_players > 0:
#             minecraft_str += "\n" + f"The server has the following players online: {', '.join(query.players.names)}"
#         await ctx.send("```" + minecraft_str + "```")
#     else:
#         await ctx.send("The server is offline.")
#
#
# @bot.slash_command(name='ip', description='Minecraft server IP address')
# async def status(ctx):
#     await ctx.send("`" + server_ip + "`")


bot.run(TOKEN)
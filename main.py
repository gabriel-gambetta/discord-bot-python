import discord
from random import randint
from time import sleep
import mensagens
import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):

    if message.author.bot or message.author.id == config.BOT_OWNER_ID:
        return

    chance = randint(1, 20)

    if chance == 20:

        if message.author.id == config.USER_A_ID:
            await message.channel.send(mensagens.userA[randint(0, len(mensagens.userA) - 1)])

        elif message.author.id == config.USER_B_ID:
            await message.channel.send(mensagens.userB[randint(0, len(mensagens.userB) - 1)])

        elif message.author.id == config.USER_C_ID:
            await message.channel.send(mensagens.userC[randint(0, len(mensagens.userC) - 1)])

        elif message.author.id == config.USER_D_ID:
            await message.channel.send(mensagens.userD[randint(0, len(mensagens.userD) - 1)])

        elif message.author.id == config.USER_F_ID:
            await message.channel.send(mensagens.userF[randint(0, len(mensagens.userF) - 1)])

        elif message.author.id == config.USER_G_ID:
            await message.channel.send(mensagens.userG[randint(0, len(mensagens.userG) - 1)])

    elif chance == 1:
        await message.channel.send(mensagens.generic[randint(0, len(mensagens.generic) - 1)])

def finish_audio(error, connection):
    print('Audio Finalizado!')
    client.loop.create_task(connection.disconnect())

@client.event
async def on_voice_state_update(member, before, after):

    if before.channel is None and after.channel:

        if member.bot or member.id == config.BOT_OWNER_ID:
            return

        if after.channel.id == config.CHANNEL_ID:

            chance = randint(1, 20)

            if member.id == config.USER_B_ID:
                connection = await after.channel.connect()

                audio = discord.FFmpegPCMAudio("yeehaircut.mp3", executable='ffmpeg-9.0-essentials_build/bin/ffmpeg.exe')
                audio.volume = 2.5

                connection.play(audio, after=lambda error:finish_audio(error, connection))

            elif chance == 20:

                sleep(10)
                connection = await after.channel.connect()

                audio = discord.FFmpegPCMAudio("bardou.mp3", executable='ffmpeg-9.0-essentials_build/bin/ffmpeg.exe')
                audio.volume = 2.5

                connection.play(audio, after=lambda error:finish_audio(error, connection))

client.run(config.DISCORD_TOKEN)
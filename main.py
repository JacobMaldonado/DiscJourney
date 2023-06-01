import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        channel = self.get_channel(1111869455711076382)  # replace with your channel's ID
        commands = [command async for command in channel.slash_commands()]
        await channel.send('/imagine someona saying hello')
        print(commands)
        imagine = next(filter(lambda x: x.name == 'imagine', commands))
        print(imagine.options)
        await imagine(channel, prompt='Hello')
        
    async def on_message(self, message):
        # only respond to ourselves
        if message.author != self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(os.getenv('DISCORD_TOKEN'))
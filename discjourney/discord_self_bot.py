import asyncio
import discord
import os
import time

class MyClient(discord.Client):

    def __init__(self, channel_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_id = channel_id

    async def on_ready(self):
        print('Logged on as', self.user)
        
    async def on_message(self, message):
        # only respond to ourselves
        if message.author != self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

    async def get_image(self, prompt):
        channel = self.get_channel(self.channel_id)
        commands = [command async for command in channel.slash_commands()]
        imagine = next(filter(lambda x: x.name == 'imagine', commands))
        interaction = await imagine(channel, prompt=prompt)
        print(interaction)

    async def get_last_message(self):
        channel = self.get_channel(self.channel_id)
        async for message in channel.history(limit=1):
            return message


async def _set_up_client(client, token):
    await client.start(token)

async def _logic_generation(client, prompt):
    while True:
        await asyncio.sleep(1)
        print(client.client_status)
        if client.client_status.value == 'online':
            print('inside')
            await client.get_image(prompt=prompt)
            await asyncio.sleep(1)
            message = await client.get_last_message()
            while _generation_is_not_done(message):
                await asyncio.sleep(1)
                message = await client.get_last_message()
            await client.close()
            return message.attachments[0].url
        
def _generation_is_not_done(message):
    # print(message)
    print(message.content)
    # print(message.attachments)
    # print(message.components)
    # print(message.embeds)
    # print(message.reactions)
    # print(message.reference)
    # print(message.mentions)
    return 'Waiting to start' in message.content or '%)' in message.content

async def _run_tasks(client, token, prompt):
    return await asyncio.gather(_set_up_client(client, token), _logic_generation(client, prompt))

def get_image_url(token, channel_id, prompt):
    loop = asyncio.get_event_loop()

    client = MyClient(channel_id=channel_id)
    result = loop.run_until_complete(_run_tasks(client, token, prompt))
    print(result[1])
    url = result[1]
    return url

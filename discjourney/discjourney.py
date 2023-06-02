
from discjourney.discord_self_bot import get_image_url
from discjourney.image_downloader import retrieve_images_as_bytes

class Discjourney:
    def __init__(self, token, channel_id):
        self.token = token
        self.channel_id = channel_id

    def get_images(self, prompt):
        url = get_image_url(self.token, self.channel_id, prompt)
        return retrieve_images_as_bytes(url)
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url):
    response = requests.get(image_url, stream=True)
    response.raise_for_status()
    image = Image.open(response.raw)
    return image

def cut_image(image):
    width, height = image.size

    # Cut image in 4 parts
    images = [
        image.crop((0, 0, width // 2, height // 2)),
        image.crop((width // 2, 0, width, height // 2)),
        image.crop((0, height // 2, width // 2, height)),
        image.crop((width // 2, height // 2, width, height))
    ]

    return images

def image_to_bytes(images):
    byte_arrays = []
    for img in images:
        byte_arr = BytesIO()
        img.save(byte_arr, format='JPEG')
        byte_arrays.append(byte_arr.getvalue())
    return byte_arrays

def process_image(image_url):
    image = download_image(image_url)
    images = cut_image(image)
    return image_to_bytes(images)

def retrieve_images_as_bytes(image_url):
    byte_arrays = process_image(image_url)
    return byte_arrays
    
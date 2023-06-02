from setuptools import setup, find_packages

setup(
    name="discjourney",
    version="0.1",
    packages=["discjourney"],
    description="Mid Journey Unoficial API to get images from Discord's Midjourney bot.",
    author="Jacob Maldonado",
    author_email="jacobmaldonado99@gmail.com",
    url="https://github.com/JacobMaldonado/DiscJourney",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        "aiohttp==3.8.4",
        "aiosignal==1.3.1",
        "async-timeout==4.0.2",
        "attrs==23.1.0",
        "certifi==2023.5.7",
        "charset-normalizer==3.1.0",
        "discord-protos==0.0.2",
        "discord.py-self==2.0.0",
        "frozenlist==1.3.3",
        "idna==3.4",
        "multidict==6.0.4",
        "Pillow==9.5.0",
        "protobuf==4.23.2",
        "requests==2.31.0",
        "urllib3==2.0.2",
        "yarl==1.9.2"
    ],
)

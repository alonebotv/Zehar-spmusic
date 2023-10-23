import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AMMusicV2 import LOGGER, app, userbot
from AMMusicV2.core.call import Aviax
from AMMusicV2.misc import sudo
from AMMusicV2.plugins import ALL_MODULES
from AMMusicV2.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AMMusicV2.plugins" + all_module)
    LOGGER("AMMusicV2.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Aviax.start()
    try:
        await Aviax.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AMMusicV2").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Aviax.decorators()
    LOGGER("AMMusicV2").info(
        "\x53\x6F\x70\x68\x69\x61\x20\x4D\x75\x73\x69\x63\x20\x42\x6F\x74\x20\x73\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79\x2E\x2E\x2E\x5C\x6E\x5C\x6E\x20\x4E\x6F\x77\x20\x4A\x6F\x69\x6E\x20\x40\x41\x62\x68\x69\x4D\x6F\x64\x73\x7A\x59\x54\x5F\x52\x65\x74\x75\x72\x6E"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AMMusicV2").info("Stopping AM Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

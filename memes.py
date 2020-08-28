# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for having some fun with people. """

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub

from collections import deque

import requests

from userbot.events import register




@register(outgoing=True, pattern=r"^\.snow$")
async def moon(event):
    deq = deque(list("🌨🌨🌨🌨🌨🌨🌨🌨"))
    deq = deque(list(" ❄️   ❄️   ❄️  ❄️   ❄️   ❄️"))
   
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


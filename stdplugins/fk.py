"""Emoji

Available Commands:

.fk"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0, 8)
    input_str = event.pattern_match.group(1)
    if input_str == "fk":
        await event.edit(input_str)
        animation_chars = [
            "💠",
            "💠💠\n💠",
            "💠💠💠\n💠\n💠",
            "💠💠💠💠\n💠\n💠\n💠💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠💠\n💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠💠\n💠\n💠",
            "💠💠💠💠💠\n💠\n💠\n💠💠💠💠\n💠\n💠\n💠"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 9])

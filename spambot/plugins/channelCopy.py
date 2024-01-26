
import asyncio
from spambot import *
from telethon import events
from telethon.tl import types



@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/chcp'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/chcp'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/chcp'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/chcp'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/chcp'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/chcp'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/chcp'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/chcp'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/chcp'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/chcp'))
async def chcp(e):
    mess = e.message.message
    cid = mess[6:]
    async for msg in e.client.iter_messages(int(cid), reverse=True):
        if not isinstance(msg, types.MessageService):
            await e.client.send_message(e.chat_id, msg)
            await asyncio.sleep(1)


#Tg:sources_cods/Am_RoBots
#Github.com/8769Anurag

"""
Plugin for both public & private channels!
"""

import time, os, asyncio

from .. import bot as Drone
from .. import userbot, Bot, AUTH
from .. import FORCESUB as fs
from main.plugins.pyroplug import check, get_bulk_msg
from main.plugins.helpers import get_link, screenshot

from telethon import events, Button, errors
from telethon.tl.types import DocumentAttributeVideo

from pyrogram import Client 
from pyrogram.errors import FloodWait

from ethon.pyfunc import video_metadata
from ethon.telefunc import force_sub

ft = f"To use this bot you've to join @{fs}."

batch = []

async def get_pvt_content(event, chat, id):
    msg = await userbot.get_messages(chat, ids=id)
    await event.client.send_message(event.chat_id, msg) 
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/batch'))
async def _batch(event):
    if not event.is_private:
        return
    # ¿Cuál es el uso de fsub aquí si el comando está destinado al propietario? 
    # Bueno soy demasiado perezosa para limpiar
    s, r = await force_sub(event.client, fs, event.sender_id, ft) 
    if s == True:
        await event.reply(r)
        return       
    if f'{event.sender_id}' in batch:
        return await event.reply("Ya comenzaste un lote, ¡espera a que se complete, tu tonto dueño!")
    async with Drone.conversation(event.chat_id) as conv: 
        if s != True:
            await conv.send_message("Envíame el enlace del mensaje desde el que deseas comenzar a guardar, como respuesta a este mensaje.", buttons=Button.force_reply())
            try:
                link = await conv.get_reply()
                try:
                    _link = get_link(link.text)
                except Exception:
                    await conv.send_message("No link found.")
            except Exception as e:
                print(e)
                return await conv.send_message("¡No puedo esperar más por tu respuesta!")
            await conv.send_message("Envíeme la cantidad de archivos/rango que desea guardar del mensaje dado, como respuesta a este mensaje.", buttons=Button.force_reply())
            try:
                _range = await conv.get_reply()
            except Exception as e:
                print(e)
                return await conv.send_message("¡No puedo esperar más por tu respuesta!")
            try:
                value = int(_range.text)
                if value > 100:
                    return await conv.send_message("Solo puede obtener hasta 100 archivos en un solo lote.")
            except ValueError:
                return await conv.send_message("¡El rango debe ser un número entero!")
            s, r = await check(userbot, Bot, _link)
            if s != True:
                await conv.send_message(r)
                return
            batch.append(f'{event.sender_id}')
            await run_batch(userbot, Bot, event.sender_id, _link, value) 
            conv.cancel()
            batch.pop(0)
            
            
async def run_batch(userbot, client, sender, link, _range):
    for i in range(_range):
        timer = 60
        if i < 25:
            timer = 5
        if i < 50 and i > 25:
            timer = 10
        if i < 100 and i > 50:
            timer = 15
        if not 't.me/c/' in link:
            if i < 25:
                timer = 2
            else:
                timer = 3
        try:
            await get_bulk_msg(userbot, client, sender, link, i) 
        except FloodWait as fw:
            await asyncio.sleep(fw.seconds + 5)
            await get_bulk_msg(userbot, client, sender, link, i)
        protection = await client.send_message(sender, f"Durmiendo por `{timer}` segundos para evitar Floodwaits y proteger la cuenta!")
        time.sleep(timer)
        await protection.delete()
            
                


import os
import sys
import config as c
import logging
from telethon import TelegramClient, custom, events, sync, errors

logging.basicConfig(level=logging.INFO)
sys.dont_write_bytecode = True


script_dir = os.path.dirname(os.path.realpath(__file__))
client = TelegramClient(os.path.join(script_dir, 'pinbot'), c.api_id, c.api_hash)



@client.on(events.ChatAction())
async def on_pin(event):
    if not event.new_pin:
        return
    # else if its a pin message:

    if event.chat_id in c.pin_chats:
        # If the chat this pin is from is in our dictionary, forward to its channel
        action_msg = event.action_message

        await client.forward_messages(
            c.pin_chats[event.chat_id],
            action_msg.reply_to_msg_id,
            event.chat_id,
            silent=True)


client.start(bot_token=c.token)
client.run_until_disconnected()

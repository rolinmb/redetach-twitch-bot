from creds import *
from util import *
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatCommand, ChatSub
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.twitch import Twitch
import asyncio
#import logging
#logging.basicConfig(level=logging.DEBUG)

USERSCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT, AuthScope.CHANNEL_MANAGE_BROADCAST]

async def on_message(msg: ChatMessage):
    print(f"{msg.user.display_name} - {msg.text}")

async def on_command(cmd: ChatCommand):
    command = cmd.name.lower()
    if command == "re":
        await cmd.reply("REEEEEEEEEEEEEEEEEEEEEEE!!!!!")
    elif command == "guh":
        await cmd.reply("GUH!")
    elif command == "detach":
        await cmd.reply("~ im ousside my bodie ~")
    elif command == "discord":
        await cmd.reply("https://discord.gg/qcsJPjQ8")
    elif command == "links":
        await cmd.reply("https://redetach-music.web.app")
    elif command == "lenny":
        await cmd.reply("( ͡° ͜ʖ ͡°)")
    else:
        await cmd.reply(f"Unknown command: {command}")

async def on_ready(ready_event: EventData):
    await ready_event.chat.join_room(TARGETCHANNEL)
    print(f"Bot has joined the channel of {TARGETCHANNEL}")

async def run_bot():
    bot = await Twitch(CLIENTID, CLIENTSECRET)
    auth = UserAuthenticator(bot, USERSCOPE, force_verify=False, host='127.0.0.1', port=17563)
    try:
        token, refresh_token = await auth.authenticate()
        print(f"Authentication successful.")
    except Exception as e:
        print(f"Authentication failed: {e}")
        return

    await bot.set_user_authentication(token, USERSCOPE, refresh_token)

    chat = await Chat(bot)

    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    chat.register_command("re", on_command)
    chat.register_command("guh", on_command)
    chat.register_command("detach", on_command)
    chat.register_command("discord", on_command)
    chat.register_command("links", on_command)
    chat.register_command("lenny", on_command)

    try:
        chat.start()
        print("Chat started successfully.")
        input("Press ENTER to stop\n")
    except Exception as e:
        print(f"Failed to start chat: {e}")
    finally:
        chat.stop()
        await bot.close()

if __name__ == "__main__":
    asyncio.run(run_bot())

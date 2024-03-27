import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

import telethon
from data import rev, add_user, conn, rm

api_id = 21745398
api_hash = "381e0a5b910b5533b40ae1b2e3b50364"
bot_token = "7118642893:AAGaLXcohyum0ExrLL8xNC3XHdXNUiR5nQM"
apicat = "live_bNM0ztnyqxNWhFDEgaYFOa2tfxjByPvkdXZQacdnmlBptflIFW1G6dGr41UbXmQw"

kai = telethon.TelegramClient("kai", api_hash=api_hash, api_id=api_id)
bot = telethon.TelegramClient("bot",  api_id=api_id, api_hash=api_hash).start(bot_token=bot_token)

async def maink():
    pass

@bot.on(telethon.events.NewMessage)
async def handler(event):
    sender = await event.get_sender()

    x = event.raw_text.split(" ")
    if ".reg" in event.raw_text and len(x) == 3:
        try:
            int(x[2])
            add_user(x[1], x[2])
            await bot.send_message(event.sender_id, "Successful :D")
        except ValueError:
            await bot.send_message(event.sender_id, "Age must be integers, no?")


    if event.sender_id == 2086959371:
        if "kyra." == event.raw_text:
            await event.reply("Yes, Kai. How can i assist you today? :D")

        if ".rm" == event.raw_text:
            rm()
            await event.reply("Done !")

        if ".exp" == event.raw_text:
            for i in rev():
                await bot.send_message(event.sender_id, f"User **{str(i[0])}**, **{str(i[1])}** years old")
            if len(rev()) == 0:
                await bot.send_message(event.sender_id, "Database is currently empty.")

    elif event.sender_id != 2086959371:
        if "kyra." == event.raw_text:
            await event.reply("What :<")
    else:
        pass


bot.run_until_disconnected()
conn.close()
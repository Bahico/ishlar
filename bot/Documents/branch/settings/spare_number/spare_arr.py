import sqlite3

import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from branch.settings.settings_main import admin_settings_main
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_spare_arr(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    spares = \
        conn.execute("select kuzif, mator, tuning from BRANCH where id = (?);", (callback_query["number"],)).fetchall()[
            0]
    awa = ""
    if callback_query["language"] == "uzb":
        if spares[0] is not None:
            awa += "Kuzif\n"
            son = 0
            for i in spares[0].split("."):
                son += 1
                i = i.split(",")
                spare = conn.execute("select kuzif from CAR where id = (?);", (int(i[1]),)).fetchall()
                if spare:
                    spare = spare[0][0]
                    awa += "  " + str(son) + ") " + i[0] + " so'mlik " + spare.split("[")[0] + "\n"
        if spares[1] is not None:
            awa += "Mator\n"
            son = 0
            for i in spares[1].split("."):
                son += 1
                i = i.split(",")
                spare = conn.execute("select mator from CAR where id = (?);", (int(i[1]),)).fetchall()[0][0]
                if spare:
                    spare = spare[0][0]
                    awa += "  " + str(son) + ") " + i[0] + " so'mlik " + spare.split("[")[0] + "\n"
        if spares[2] is not None:
            awa += "Tuning\n"
            son = 0
            for i in spares[1].split("."):
                son += 1
                i = i.split(",")
                spare = conn.execute("select mator from CAR where id = (?);", (int(i[1]),)).fetchall()[0][0]
                if spare:
                    spare = spare[0][0]
                    awa += "  " + str(son) + ") " + i[0] + " so'mlik " + spare.split("[")[0] + "\n"
        if awa == "":
            await bot.send_message(message.from_user.id, "Siz hali hech nima qo'shmadingiz!")
        else:
            await bot.send_message(message.from_user.id, awa)

    await admin_settings_main(message, vote_cb, callback_query)

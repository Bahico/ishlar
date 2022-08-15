import sqlite3

import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from ..basket.basket_main import client_basket
from ..basket.reduce import \
    client_reduce_add, client_reduce_del, client_reduce_remove_all, \
    client_reduce_reduce, client_reduce_arrived, client_reduce_info
from ..car_arr.car_name import client_car_name, client_name_bypass
from ..car_arr.print_car_spare import client_print_car
from ..menu.language import client_edit_language, client_language_edit
from ..menu.menu import client_menu
from ..menu.phone_number import client_edit_phone_number
from ..my_settings import client_phone_number
from ..spare.print_spare_number import client_print_spare_number, client_spare_button_number
from ..spare.spare_main import client_spare_number

from config import TOKEN

# some code

# "id", "language", "action"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_client_callback(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    if callback_query["id"] == "start":
        if callback_query["stage"] == "start":
            await client_phone_number(message, conn, callback_query)

        elif callback_query["stage"] == "start_arr":
            if callback_query["name"] == "basket":
                await client_basket(message, conn, vote_cb, callback_query)
            else:
                await client_car_name(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "car name":
            if callback_query["name"] == "bypass":
                await client_name_bypass(message, conn, vote_cb, callback_query)
            else:
                await client_print_car(message, conn, vote_cb, callback_query)

        elif callback_query["stage"] == "tuning":
            await client_spare_number(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "mator":
            await client_spare_number(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "kuzif":
            await client_spare_number(message, conn, vote_cb, callback_query)

    elif callback_query["id"] == "spare_menu":
        if callback_query["stage"] == "+":
            await client_reduce_add(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "-":
            await client_reduce_reduce(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "delete":
            await client_reduce_del(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "remove_all":
            await client_reduce_remove_all(message, conn, vote_cb, callback_query)
        # elif callback_query["stage"] == "send":
        #     await client_reduce_send(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "info":
            await client_reduce_info(message, conn, vote_cb, callback_query)

    elif callback_query["id"] == "spare":
        if callback_query["stage"] == "arrived":
            await client_reduce_arrived(message, conn, callback_query)
        else:
            await client_print_spare_number(message, conn, vote_cb, callback_query)
    elif callback_query["id"] == "spare_":
        await client_spare_button_number(message, conn, vote_cb, callback_query)

    elif callback_query["id"] == "main_menu":
        if callback_query["stage"] == "history":
            pass
        elif callback_query["stage"] == "language_edit":
            await client_edit_language(message, vote_cb, callback_query)
        elif callback_query["stage"] == "phone_number":
            await client_edit_phone_number(message, conn, callback_query)
        elif callback_query["stage"] == "language_add":
            await client_language_edit(message, conn, vote_cb, callback_query)
        elif callback_query["stage"] == "back":
            await client_menu(message, conn, vote_cb, callback_query["language"])
    conn.commit()

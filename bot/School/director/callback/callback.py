from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN
from director.admin.add import director_admin_login

from director.menu.admin import director_admin_menu
from director.menu.attend import director_attend_menu, director_attend_lifetime
from director.menu.menu import director_main_menu
from director.start.start import director_start_district, director_start_school, director_start_code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def director_callback(message:types.Message,district_conn,director_conn,family_conn,attend_conn,conn,vote_cb,callback_query):
    if callback_query["province"] == "stop":
        if callback_query["name"] == "stop":
            await director_main_menu(message, conn, vote_cb)

    elif callback_query["province"] == "start":
        if callback_query["name"] == "province":
            await director_start_district(message,district_conn,vote_cb,callback_query)
        elif callback_query["name"] == "city":
            await director_start_school(message,director_conn,vote_cb,callback_query)
        elif callback_query["name"] == "school":
            await director_start_code(message, conn, family_conn, callback_query)

    elif callback_query["province"] == "main menu":
        if callback_query["name"] == "admin":
            await director_admin_menu(message, vote_cb)
        elif callback_query["name"] == "attend":
            await director_attend_menu(message, vote_cb)
        else:
            pass

    # elif callback_query["province"] == "attend":
    #     if callback_query["name"] == "type tur":
    #         await director_attend_lifetime(message, vote_cb, callback_query)
    #     elif callback_query["name"] == "type lifetime":
    #         await director_attend_year(message,director_conn,attend_conn,conn, vote_cb, callback_query)
    #     elif callback_query["name"] == "type year":
    #         await director_attend_month(message, attend_conn, conn, vote_cb, callback_query)
    #     elif callback_query["name"] == "type month":
    #         await director_attend_day(message, attend_conn, conn, vote_cb, callback_query)
    #     elif callback_query["name"] == "type day":
    #         if callback_query["clas"] == "school":
    #             await director_attend_school(message, attend_conn, conn, vote_cb, callback_query)

    elif callback_query["province"] == "admin":
        if callback_query["name"] == "+":
            await director_admin_login(message, conn, vote_cb)
        else:
            pass
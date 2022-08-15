from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from family.menu.children import family_children, family_student_menu
from family.menu.menu import family_main_menu
from family.start.start import family_city, family_school, family_class_number, family_class_name, family_student, \
    family_code, family_governor

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def family_callback(message:types.Message,governor_conn,district_conn,director_conn,class_conn,student_conn,family_conn,conn,vote_cb,callback_query):
    if callback_query["province"] == "stop":
        if callback_query["name"] == "stop":
            await family_main_menu(message, conn, vote_cb)

    elif callback_query["province"] == "start":
        if callback_query["name"] == "governor":
            await family_city(message,district_conn,director_conn,class_conn,vote_cb,callback_query["school"],callback_query["city"])
        elif callback_query["name"] == "city":
            await family_school(message,director_conn,class_conn,vote_cb,callback_query["school"],callback_query["city"])
        elif callback_query["name"] == "school":
            await family_class_number(message,class_conn,vote_cb,callback_query["school"],callback_query["city"])
        elif callback_query["name"] == "class number":
            await family_class_name(message,class_conn,vote_cb,callback_query["school"],callback_query["city"])
        elif callback_query["name"] == "class name":
            await family_student(message,student_conn,vote_cb, callback_query)
        elif callback_query["name"] == "student":
            await family_code(message,family_conn,conn, callback_query)

    elif callback_query["province"] == "main menu":
        if callback_query["name"] == "student":
            await family_children(message, family_conn, student_conn, vote_cb)
        else:
            await bot.send_message(message.from_user.id,"Hali bu funksiya ishlamayapti")

    elif callback_query["province"] == "children":
        if callback_query["name"] == "student":
            if callback_query["city"] == "new":
                await family_governor(message,governor_conn, district_conn, director_conn, class_conn, vote_cb)
            else:
                await family_student_menu(message, vote_cb, callback_query)
        elif callback_query["name"] == "delete":
            pass
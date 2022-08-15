from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN

# some code
from teacher.attend.attend import teacher_attend_number, teacher_attend_name, teacher_attend_lesson, teacher_attend_arr, \
    teacher_attend_del, teacher_attend_del_, teacher_attend_finish, teacher_attend_fan
from teacher.fan.fan import teacher_fan_insert, teacher_fan_new_add, teacher_fan_new
from teacher.menu.fan import teacher_menu_fan
from teacher.menu.menu import teacher_main_menu
from teacher.menu.settings import teacher_settings_menu, teacher_settings_edit_code
from teacher.start.start import teacher_city, teacher_school, teacher_fan, teacher_teachers, teacher_teacher

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def teacher_callback(message:types.Message,district_conn,director_conn,teacher_conn,family_conn,class_conn,attend_conn,student_conn,conn,vote_cb,callback_query):
    if callback_query["province"] == "stop":
        if callback_query["name"] == "stop":
            await teacher_main_menu(message, conn, vote_cb)

    elif callback_query["province"] == "start":
        if callback_query["name"] == "province":
            await teacher_city(message,district_conn,vote_cb, callback_query)
        elif callback_query["name"] == "city":
            await teacher_school(message,director_conn,vote_cb, callback_query)
        elif callback_query["name"] == "school":
            await teacher_fan(message,teacher_conn,vote_cb,callback_query)
        elif callback_query["name"] == "fan":
            await teacher_teachers(message,teacher_conn,vote_cb, callback_query)
        elif callback_query["name"] == "my":
            await teacher_teacher(message,family_conn,conn,callback_query)

    elif callback_query["province"] == "main menu":
        if callback_query["name"] == "attend":
            await teacher_attend_number(message, teacher_conn, class_conn, attend_conn, vote_cb)
        elif callback_query["name"] == "fan":
            await teacher_menu_fan(message, teacher_conn, conn, vote_cb)
        elif callback_query["name"] == "my setting":
            await teacher_settings_menu(message, vote_cb)

    elif callback_query["province"] == "settings":
        if callback_query["name"] == "edit code":
            await teacher_settings_edit_code(message, conn, vote_cb)

    elif callback_query["province"] == "attend":
        if callback_query["name"] == "class number":
            await teacher_attend_name(message, class_conn, vote_cb, callback_query)
        elif callback_query["name"] == "class name":
            await teacher_attend_lesson(message, attend_conn, vote_cb, callback_query)
        elif callback_query["name"] == "lesson":
            await teacher_attend_arr(message, student_conn, attend_conn, vote_cb, callback_query)
        elif callback_query["name"] == "student":
            await teacher_attend_del(message, teacher_conn, student_conn, attend_conn, vote_cb, callback_query)
        elif callback_query["name"] == "student_":
            await teacher_attend_del_(message, teacher_conn, student_conn, attend_conn, vote_cb, callback_query)
        elif callback_query["name"] == "finish":
            await teacher_attend_fan(message, teacher_conn, vote_cb, callback_query)
        elif callback_query["name"] == "fan":
            await teacher_attend_finish(message, attend_conn, conn, vote_cb, callback_query)
    elif callback_query["province"] == "fan":
        if callback_query["name"] == "add":
            await teacher_fan_insert(message, teacher_conn, conn, vote_cb, callback_query)
        elif callback_query["name"] == "new add":
            await teacher_fan_new_add(message, conn, vote_cb)
        elif callback_query["name"] == "new":
            await teacher_fan_new(message, teacher_conn, vote_cb)
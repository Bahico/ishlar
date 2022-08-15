from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from admin.attend.attend import attend_today_number, attend_today_name, attend_today_arr, attend_today_reason, \
    attend_today_student, attend_today_finish, attend_today_student_
from admin.menu.clas import admin_class
from admin.menu.menu import admin_main_menu
from admin.menu.student import admin_student
from admin.menu.teacher import admin_teacher_menu, admin_teacher_class
from admin.student.add import admin_class_number, admin_class_name, admin_student_last
from admin.student.add_class import admin_class_new_number, admin_class_tur, admin_class_number_add
from admin.teacher.add import admin_teacher_number, admin_teacher_fan, admin_teacher_name, admin_teacher_code, \
    admin_teacher_fan_start
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_callback(message: types.Message, admin_conn, class_conn, attend_conn, student_conn, teacher_conn, conn, vote_cb, callback_query):
    if callback_query["province"] == "stop":
        if callback_query["name"] == "stop":
            await admin_main_menu(message, conn, vote_cb)

    elif callback_query["province"] == "menu":
        if callback_query["name"] == "main menu":
            await admin_main_menu(message, conn, vote_cb)

    elif callback_query["province"] == "main menu":
        if callback_query["name"] == "student":
            await admin_student(message, vote_cb)
        elif callback_query["name"] == "teacher":
            await admin_teacher_menu(message, vote_cb)
        elif callback_query["name"] == "class":
            await admin_class(message, vote_cb)
        elif callback_query["name"] == "attend":
            await attend_today_number(message, admin_conn, attend_conn, class_conn, vote_cb)
        else:
            pass

    elif callback_query["province"] == "attend":
        if callback_query["name"] == "class number":
            await attend_today_name(message, class_conn, vote_cb, callback_query)
        elif callback_query["name"] == "class name":
            await attend_today_arr(message, student_conn, attend_conn, vote_cb, callback_query)
        elif callback_query["name"] == "student":
            await attend_today_reason(message, vote_cb, callback_query)
        elif callback_query["name"] == "student_":
            await attend_today_student_(message, student_conn, attend_conn, vote_cb, callback_query)
        elif callback_query["name"] == "reason":
            await attend_today_student(message, student_conn, attend_conn, vote_cb, callback_query)
        elif callback_query["name"] == "no reason":
            await attend_today_student(message, student_conn, attend_conn, vote_cb, callback_query)
        elif callback_query["name"] == "finish":
            await attend_today_finish(message, class_conn, attend_conn, admin_conn, vote_cb, callback_query)

    elif callback_query["province"] == "student":
        if callback_query["name"] == "+":
            await admin_class_number(message, admin_conn, class_conn, conn, vote_cb)
        else:
            pass

    elif callback_query["province"] == "add student":
        if callback_query["name"] == "class number":
            await admin_class_name(message, class_conn, vote_cb, callback_query)
        elif callback_query["name"] == "class name":
            await admin_student_last(message, admin_conn, conn, vote_cb, callback_query)


    elif callback_query["province"] == "teacher":
        if callback_query["name"] == "+":
            await admin_teacher_class(message, vote_cb)
        elif callback_query["name"] == "class":
            await admin_teacher_number(message, admin_conn, class_conn, vote_cb)
        elif callback_query["name"] == "fan":
            await admin_teacher_fan(message,admin_conn, teacher_conn, vote_cb, callback_query)

    elif callback_query["province"] == "add teacher":
        if callback_query["name"] == "class number":
            await admin_teacher_name(message, class_conn, vote_cb, callback_query)
        elif callback_query["name"] == "class name":
            await admin_teacher_fan(message, admin_conn, teacher_conn, vote_cb, callback_query)
        elif callback_query["name"] == "add fan":
            await admin_teacher_code(message, admin_conn, conn, vote_cb, callback_query)
        elif callback_query["name"] == "new fan":
            await admin_teacher_fan_start(message, conn)

    elif callback_query["province"] == "class":
        if callback_query["name"] == "+":
            await admin_class_number_add(message, class_conn, conn, vote_cb)
        elif callback_query["name"] == "number":
            if callback_query["city"] == "new":
                await admin_class_new_number(message, conn)
            else:
                await admin_class_tur(message, conn)
        else:
            await bot.send_message(message.from_user.id,"Hali bu funksiya ishlamayapti")


from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from admin.student.add import admin_student_first, admin_student_father, admin_student_mother, admin_student_family, \
    admin_student_code
from admin.student.add_class import admin_class_insert
from admin.teacher.add import admin_teacher_first, admin_teacher_last, admin_teacher_insert, \
    admin_teacher_fan_insert
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def admin_message(message:types.Message,admin_conn,student_conn,teacher_conn,class_conn,conn,admin,vote_cb):
    if admin[1] == "add student first name":
        await admin_student_first(message, admin_conn, conn)
    elif admin[1] == "add student last name":
        await admin_student_father(message,admin_conn, student_conn, conn, vote_cb)
    elif admin[1] == "add student father":
        await admin_student_mother(message, admin_conn, conn)
    elif admin[1] == "add student mother":
        await admin_student_family(message, admin_conn, student_conn, conn)
    elif admin[1] == "add teacher fan":
        await admin_teacher_fan_insert(message, admin_conn, teacher_conn, conn, vote_cb)
    elif admin[1] == "add teacher code":
        await admin_teacher_first(message, admin_conn, teacher_conn, conn, vote_cb)
    elif admin[1] == "add teacher first":
        await admin_teacher_last(message, admin_conn, conn, vote_cb)
    elif admin[1] == "add teacher last":
        await admin_teacher_insert(message, admin_conn, teacher_conn, conn, vote_cb)
    elif admin[1] == "add class number":
        await admin_class_insert(message, class_conn, conn, vote_cb, admin_conn)
    elif admin[1] == "add class tur":
        await admin_class_insert(message, class_conn, conn, vote_cb, admin_conn)
    elif admin[1] == "add student code":
        await admin_student_code(message, admin_conn, student_conn, conn, vote_cb)
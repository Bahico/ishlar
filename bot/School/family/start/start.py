from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# some code
from family.menu.menu import family_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def family_governor(message:types.Message,governor_conn,district_conn,director_conn,class_conn,vote_cb):
    governor = governor_conn.execute("select name, number from CONN;").fetchall()
    if len(governor) != 1:
        markup = InlineKeyboardMarkup(reply_markup=True)
        markup.row_width = 2
        for i in governor:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="governor", province="start",city=i[1], school=i[0], tur="None",clas="None", action="family")))
        await message.answer("Bolangiz qaysi viloyatda o'qidi?",reply_markup=markup)
    else:
        await family_city(message,district_conn,director_conn,class_conn,vote_cb,governor[0][0],governor[0][1])

async def family_city(message:types.Message,district_conn,director_conn,class_conn,vote_cb,name,id):
    district = district_conn.execute("select name, number from CONN where id = (?);",(id,)).fetchall()
    if len(district) != 1:
        markup = InlineKeyboardMarkup(reply_markup=True)
        markup.row_width = 2
        for i in district:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="city", province="start",city=i[1], school=i[0], tur="None",clas="None", action="family")))
        await bot.send_message(message.from_user.id,f"Bolangiz {name} viloyatidagi qaysi tumanda o'qidi?",reply_markup=markup)
    else:
        await family_school(message, director_conn, class_conn, vote_cb, district[0][1], district[0][0])

async def family_school(message:types.Message,director_conn,class_conn,vote_cb,name,id):
    school = director_conn.execute("select name, number from CONN where id = (?);",(id,)).fetchall()
    if len(school) != 1:
        markup = InlineKeyboardMarkup(reply_markup=True)
        markup.row_width = 2
        for i in school:
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="school", province="start",city=i[1], school=i[0], tur="None",clas="None", action="family")))
        await bot.send_message(message.from_user.id,f"Bolangiz {name} tumanidagi qaysi maktabda o'qidi?",reply_markup=markup)
    else:
        await family_class_number(message, class_conn, vote_cb, school[0][1], school[0][0])

async def family_class_number(message:types.Message,class_conn,vote_cb,name,id):
    class_number = class_conn.execute("select name, number from NUMBER where id = (?);",(id,)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    for i in class_number:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class number", province="start",city=i[1], school=i[0], tur="None",clas="None", action="family")))
    await bot.send_message(message.from_user.id,f"Bolangiz {str(name)} maktabidagi nechinchi sinfda o'qidi?",reply_markup=markup)

async def family_class_name(message:types.Message,class_conn,vote_cb,name,id):
    class_name = class_conn.execute("select name, number from NAME where id = (?);",(id,)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    for i in class_name:
        markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="class name", province="start",city=i[1], school=i[0], tur="None",clas="None", action="family")))
    await bot.send_message(message.from_user.id,f"Bolangiz {str(name)}-sinflardagi qaysi sinfda o'qidi?",reply_markup=markup)

async def family_student(message:types.Message,student_conn,vote_cb,callback_query):
    student = student_conn.execute("select first_name, last_name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 2
    for i in student:
        markup.insert(InlineKeyboardButton(text=f"{i[0]} {i[1]}",callback_data=vote_cb.new(name="student", province="start",city=i[2], school=callback_query["city"], tur=i[1],clas=i[0], action="family")))
    await bot.send_message(message.from_user.id,"Bolangizni tanlang",reply_markup=markup)

async def family_code(message:types.Message,family_conn,conn,callback_query):
    family = family_conn.execute("select * from SAVE where id = (?);",(message.from_user.id,)).fetchall()
    if not family:
        family_conn.execute("insert into SAVE(id,name,name_text) values (?,?,?);",(message.from_user.id,callback_query["city"],callback_query["school"]))
        conn.execute("insert into SAVE(id,name,text) values (?,'family','code');",(message.from_user.id,))
    else:
        family_conn.execute(f"update SAVE set name = (?), name_text = '{callback_query['school']}' where id = (?);",(callback_query["city"],message.from_user.id))
        conn.execute("update SAVE set text = 'code_' where id = (?);",(message.from_user.id,))
    await bot.send_message(message.from_user.id,f"{callback_query['clas']} {callback_query['tur']} ning kodini kiriting")

async def family_insert(message:types.Message,student_conn,family_conn,director_conn,conn):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    family = family_conn.execute("select name, test, name_text from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    test = family[1]
    student = student_conn.execute("select code from CODE where id = (?);",(family[0],)).fetchall()[0][0]
    if test > 0:
        if message.text == student:
            await message.answer("Qabul qilindi")
            family_conn.execute("update SAVE set name = NULL where id = (?);",(message.from_user.id,))
            family_conn.execute("insert into CHILDREN(id,student) values (?,?);",(message.from_user.id,family[0]))
            director_conn.execute("insert into FAMILY(id,school) values (?,?);",(message.from_user.id,int(family[2])))
            conn.execute("update SAVE set text = 'contact' where id = (?);",(message.from_user.id,))
            markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("❌Telefon raqamim",request_contact=True))
            await message.answer("Telefon raqamingizni kiriting",reply_markup=markup)
            await bot.delete_message(message.from_user.id,message.message_id+1)
        else:
            family_conn.execute("update SAVE set test = (?) where id = (?);",(test-1,message.from_user.id))
            await message.answer(f"Iltimos togri kiriting\n\nSizda {str(test-1)} imkoniyati bor")
    else:
        family_conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
        conn.execute("delete from SAVE where id = (?);",(message.from_user.id,))
        await message.answer("Iltimos botda tog'ri foydalaning")

async def family_add_children(message:types.Message,student_conn,family_conn,director_conn,conn,vote_cb):
    try: await bot.delete_message(message.from_user.id,message.message_id-1)
    except: pass
    family = family_conn.execute("select name, test, name_text from SAVE where id = (?);",(message.from_user.id,)).fetchall()[0]
    test = family[1]
    student = student_conn.execute("select code from CODE where id = (?);",(family[0],)).fetchall()[0][0]
    if test > 0:
        if message.text == student:
            await message.answer("Qabul qilindi")
            family_conn.execute("update SAVE set name = NULL, name_text = NULL where id = (?);",(message.from_user.id,))
            family_conn.execute("insert into CHILDREN(id,student) values (?,?);",(message.from_user.id,family[0]))
            conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
            await family_main_menu(message, vote_cb)
            await bot.delete_message(message.from_user.id,message.message_id+1)
        else:
            family_conn.execute("update SAVE set test = (?) where id = (?);",(test-1,message.from_user.id))
            await message.answer(f"Iltimos togri kiriting\n\nSizda {str(test-1)} imkoniyati bor")
    else:
        family_conn.execute("update SAVE set name = NULL, name_text = NULL where id = (?);",(message.from_user.id,))
        conn.execute("update SAVE set text = NULL where id = (?);",(message.from_user.id,))
        await message.answer("Iltimos kodni to'g'ri kiriting")
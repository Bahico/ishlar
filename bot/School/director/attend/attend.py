from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from config import TOKEN

# some code
from director.menu.menu import director_main_menu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def director_attend_year(message:types.Message,director_conn,attend_conn,class_conn,conn,vote_cb,callback_query):
    director = director_conn.execute("select name from USER where id = (?);",(message.from_user.id,)).fetchall()[0][0]
    director = director_conn.execute("select id from CONN where number = (?);",(director,)).fetchall()[0][0]
    year = attend_conn.execute("select date, escape_, leave, for_no_reason, for_reason from SCHOOL where id = (?);",(director,)).fetchall()
    if not year:
        await bot.send_message(message.from_user.id,"Hali maktabingizda dars o'tilmagan")
        await director_main_menu(message,conn,vote_cb)
    else:
        year_set = set()
        for i in year:
            year_set.add(i[0].split("/")[1])
        if len(year_set) == 1:
            if callback_query["tur"] == "year":
                if callback_query["clas"] == "school":
                    await director_attend_school_year(message, attend_conn, conn, vote_cb, callback_query, director)
                else:
                    await director_attend_class_number(message, class_conn, vote_cb, callback_query)
            else:
                son = None
                for i in year_set:
                    son = i
                callback_query["city"] = son
                callback_query["school"] = director
                await director_attend_month(message, attend_conn, class_conn, conn, vote_cb, callback_query)
        else:
            markup = InlineKeyboardMarkup(reply_markup=True,row_width=2)
            for i in year_set:
                markup.insert(InlineKeyboardButton(text="20"+i,callback_data=vote_cb.new(name="type year",province="attend",city=i,school=director,tur=callback_query["tur"],clas=callback_query["clas"],action="director")))
            await bot.send_message(message.from_user.id,"Nechinchi yilni tekshirmoqchisiz?",reply_markup=markup)

async def director_attend_month(message:types.Message,attend_conn,class_conn,conn,vote_cb,callback_query):
    if callback_query["tur"] == "year":
        if callback_query["clas"] == "school":
            await director_attend_school_year(message, attend_conn, conn, vote_cb, callback_query)
        else:
            await director_attend_class_number(message, class_conn, vote_cb, callback_query)
    else:
        month = attend_conn.execute("select date from SCHOOL where id = (?);",(callback_query["school"],)).fetchall()
        markup = InlineKeyboardMarkup(reply_markup=True,row_width=2)
        for i in month:
            i = i[0].split("/")
            if i[1] == callback_query["city"]:
                markup.insert(InlineKeyboardButton(text=i[0]+"-oy",callback_data=vote_cb.new(name="type month",province="attend",city=i[0]+"/"+i[1],school=callback_query["school"],tur=callback_query["tur"],clas=callback_query["clas"],action="director")))
        await bot.send_message(message.from_user.id,"Nechinchi oyni tekshirmoqchisiz?",reply_markup=markup)


async def director_attend_day(message:types.Message,attend_conn,class_conn,conn,vote_cb,callback_query):
    if callback_query["tur"] == "month":
        if callback_query["clas"] == "school":
            await director_attend_school_month(message, attend_conn, conn, vote_cb, callback_query)
        else:
            await director_attend_class_number(message,class_conn,vote_cb, callback_query)
    else:
        day = attend_conn.execute(f"select date from CLASS where id = (?) and date like '%{callback_query['city']}';",(callback_query["school"],)).fetchall()
        day_set = set()
        for i in day:
            day_set.add(i[0].split("/")[1])
        markup = InlineKeyboardMarkup(reply_markup=True,row_width=3,inline_keyboard=True)
        for i in day_set:
            markup.insert(InlineKeyboardButton(text=i+"-kun",callback_data=vote_cb.new(name="type day",province="attend",city=callback_query["city"]+"/"+i,school=callback_query["school"],tur=callback_query["tur"],clas=callback_query["clas"],action="director")))
        await bot.send_message(message.from_user.id,"Nechinchi kunni tekshirmoqchisiz?",reply_markup=markup)


async def director_attend_class_number(message:types.Message,class_conn,vote_cb,callback_query):
    classes = class_conn.execute("select name, number from NUMBER where id = (?);",(callback_query["school"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in classes:
        markup.insert(InlineKeyboardButton(text=str(i[0]),callback_data=vote_cb.new(name="class number",province="attend",city=i[1],school=callback_query["city"],tur=callback_query["tur"],clas=callback_query["clas"],action="director")))
    await bot.send_message(message.from_user.id,"Nechinchi sinf davomatini tekshirmoqchisiz?",reply_markup=markup)

async def director_attend_class_name(message:types.Message,class_conn,vote_cb,callback_query):
    classes = class_conn.execute("select name, number from NAME where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in classes:
        markup.insert(InlineKeyboardButton(text=str(i[0]),callback_data=vote_cb.new(name="class name",province="attend",city=i[1],school=callback_query["school"],tur=callback_query["tur"],clas=callback_query["clas"],action="director")))
    await bot.send_message(message.from_user.id,"Qaysi sinfi davomatini tekshirmoqchisiz?",reply_markup=markup)

async def director_attend_class_arr(message:types.Message,student_conn,vote_cb,callback_query):
    class_arr = student_conn.execute("select first_name, last_name, number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in class_arr:
        markup.insert(InlineKeyboardButton(text=f"{i[0]} {i[1]}",callback_data=vote_cb.new(name="class arr",province="attend",city=i[1],school=callback_query["school"],tur=callback_query["tur"],clas=callback_query["clas"],action="director")))
    await bot.send_message(message.from_user.id,"Qaysi o'quvchini davomatini tekshirmoqchisiz?",reply_markup=markup)

async def director_attend_school_year(message:types.Message,attend_conn,conn,vote_cb,callback_query,director=None):
    if director is None:year = attend_conn.execute("select date, escape_, leave, for_no_reason, for_reason from SCHOOL where id = (?);",(callback_query["school"],)).fetchall()
    else: year = attend_conn.execute("select date, escape_, leave, for_no_reason, for_reason from SCHOOL where id = (?);",(director,)).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    if director is None:
        for i in year:
            if i.split("/")[0] == callback_query["city"]:
                if i[1] is not None:escape += i[1]
                if i[2] is not None:leave += i[2]
                if i[3] is not None:for_no_reason += i[3]
                if i[4] is not None:for_reason += i[4]
    else:
        for i in year:
            if i[1] is not None:escape += i[1]
            if i[2] is not None:leave += i[2]
            if i[3] is not None:for_no_reason += i[3]
            if i[4] is not None:for_reason += i[4]
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)

async def director_attend_school_month(message:types.Message,attend_conn,conn,vote_cb,callback_query):
    month = attend_conn.execute("select date, escape_, leave, for_no_reason, for_reason  from SCHOOL where id = (?);",(callback_query["school"],)).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    for i in month:
        if i[0] == callback_query["city"]:
            if i[1] is not None:escape += i[1]
            if i[2] is not None:leave += i[2]
            if i[3] is not None:for_no_reason += i[3]
            if i[4] is not None:for_reason += i[4]
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)

async def director_attend_school_day(message:types.Message,attend_conn,conn,vote_cb,callback_query):
    day = attend_conn.execute("select name from STUDENT where school = (?) and date = (?);",(callback_query["school"],callback_query["city"])).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    for i in day:
        # qob ketganda shu yerda o'quvchilarni userlari
        if i[0] == "escape":
            escape += 1
        else:
            leave += 1
            if i[0] == "reason":
                for_reason += 1
            else:
                for_no_reason += 1
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)

async def director_attend_class_year(message:types.Message,student_conn,attend_conn,conn,vote_cb,callback_query):
    class_arr = student_conn.execute("select number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    for i in class_arr:
        student = attend_conn.execute(f"select name from STUDENT where id = (?) and date like '%/{callback_query['school']}/%';",(i[0],)).fetchall()
        for i in student:
            if i[0] == "escape":
                escape += 1
            else:
                leave += 1
                if i[0] == "reason":
                    for_reason += 1
                else:
                    for_no_reason += 1
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)

async def director_attend_class_month(message:types.Message,student_conn,attend_conn,conn,vote_cb,callback_query):
    class_arr = student_conn.execute("select number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    for i in class_arr:
        student = attend_conn.execute(f"select name from STUDENT where id = (?) and date like '{callback_query['school']}/%';",(i[0],)).fetchall()
        for i in student:
            if i[0] == "escape":
                escape += 1
            else:
                leave += 1
                if i[0] == "reason":
                    for_reason += 1
                else:
                    for_no_reason += 1
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)

async def director_attend_class_day(message:types.Message,student_conn,attend_conn,conn,vote_cb,callback_query):
    class_arr = student_conn.execute("select number from CONN where id = (?);",(callback_query["city"],)).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    for i in class_arr:
        student = attend_conn.execute(f"select name from STUDENT where id = (?) and date = (?);",(i[0],callback_query["school"])).fetchall()
        for i in student:
            if i[0] == "escape":
                escape += 1
            else:
                leave += 1
                if i[0] == "reason":
                    for_reason += 1
                else:
                    for_no_reason += 1
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)

async def director_attend_student_year(message:types.Message,attend_conn,conn,vote_cb,callback_query,director=None):
    if callback_query["school"] == "all": student = attend_conn.execute(f"select name from STUDENT where id = (?);",(callback_query["city"])).fetchall()
    else: student = attend_conn.execute(f"select name from STUDENT where id = (?) and date like '%/{callback_query['school']}/%';",(callback_query["city"],)).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    for i in student:
        if i[0] == "escape":
            escape += 1
        else:
            leave += 1
            if i[0] == "reason":
                for_reason += 1
            else:
                for_no_reason += 1
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)

async def director_attend_student_month(message:types.Message,attend_conn,conn,vote_cb,callback_query):
    student = attend_conn.execute(f"select name from STUDENT where id = (?) and date like '{callback_query['school']}/%';",(callback_query["city"],)).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    for i in student:
        if i[0] == "escape":
            escape += 1
        else:
            leave += 1
            if i[0] == "reason":
                for_reason += 1
            else:
                for_no_reason += 1
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)

async def director_attend_student_day(message:types.Message,attend_conn,conn,vote_cb,callback_query):
    student = attend_conn.execute(f"select name from STUDENT where id = (?) and date = (?);",(callback_query["city"],callback_query["school"])).fetchall()
    escape = 0
    leave = 0
    for_no_reason = 0
    for_reason = 0
    for i in student:
        if i[0] == "escape":
            escape += 1
        else:
            leave += 1
            if i[0] == "reason":
                for_reason += 1
            else:
                for_no_reason += 1
    awa = "Darsdan qo'chishlar soni: "+str(escape)+"\nDarsga kelmasliklar soni: "+str(leave)+"\nSababsiz kelmasliklar soni: "+str(for_no_reason)+"\nSabablik kelmasliklar soni: "+str(for_reason)
    await bot.send_message(message.from_user.id,awa)
    await director_main_menu(message, conn, vote_cb)
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_add(message: types.Message, conn, admin):
    """
    Admindan yangi extiyot qism qabul qiladi
    :param admin:
    :param message:
    :param conn:
    :return: yangi malumot qo'shadi
    """
    add = message.text
    add = add.split(",")
    car = conn.execute("select spare, tur from ADMIN_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    snow = conn.execute("select number, branches from SPARE where id = (?) and spare_name = (?) and tur = (?);",(car[0],add[0],car[1])).fetchall()
    if snow:
        conn.execute(f"update SPARE set branches = '{snow[1]+'.'+admin[2]+','+add[1].strip()}' where number = (?);",(snow[0],))
        add = 1
    else:
        conn.execute("insert into SPARE(id,tur,spare_name,branches) values (?,?,?,?);",(car[0],car[1],add[0],str(admin[1])+','+add[1].strip()))
        spare = conn.execute(f"select number from SPARE where id = {car[0]} and tur = '{car[1]}' and spare_name = '{add[0]}' and branches = '{str(admin[1])+','+add[1]}'").fetchall()[0][0]
        conn.execute(f"update admin set settings = 'spare photo' where id = (?);",(message.from_user.id,))
        conn.execute("update ADMIN_ set spare = (?) where id = (?);",(spare,message.from_user.id))
        add = 2


    if admin[3] == "uzb":
        if add == 1: await bot.send_message(message.from_user.id,"Qo'shildi✅")
        else: await bot.send_message(message.from_user.id,"Maxsulot rasmini yuboring")
    elif admin[3] == "eng":
        if add == 1: await bot.send_message(message.from_user.id,"Added✅")
        else: pass
    elif admin[3] == "rus":
        if add == 1: await bot.send_message(message.from_user.id,"Добавлено✅")
        else: pass
    conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))



async def admin_add_callback(message: types.Message, conn, vote_cb, callback_query):
    admin = conn.execute("select spare from ADMIN_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    spare = conn.execute(f"select spare_name, number from SPARE where id = (?) and tur = '{callback_query['stage']}';",(admin[0],)).fetchall()
    son = 0
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    for i in spare:
        son = 1
        markup.add(InlineKeyboardButton(text=i[0].split("[")[0], callback_data=vote_cb.new(stage=callback_query["stage"], id="spare_+", name=i[1], number="None", language=callback_query["language"], action="branch")))
    if callback_query["language"] == "uzb":
        if son == 1:
            await bot.send_message(message.from_user.id,"Filialingizga qaysi maxsulotdan qo'shmoqchisiz🤨\n\n🧐Yoki yangi qo'shiladigan maxsulot nomini shu ko'rinishida yozing: Nomi,narxi",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Filialingizga yangi qo'shiladigan maxsulotni shu ko'rinishida yozing: Nomi,narxi")

    elif callback_query["language"] == "eng":
        if son == 1:
            await bot.send_message(message.from_user.id,"Which product do you want to add to your branch🤨\n\n🧐Or type the name of the new product to be added in this view: Name,price",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Write a new product to be added to your branch in the following form: Name,price")

    elif callback_query["language"] == "rus":
        if son == 1:
            await bot.send_message(message.from_user.id,"Какой продукт вы хотите добавить в свою ветку🤨\n\n🧐Или введите имя нового продукта, который будет добавлен в этом представлении: Название,цена",reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"Напишите новый продукт, который будет добавлен в вашу ветку в следующей форме: Название,цена")
    conn.execute(f"update ADMIN_ set spare = (?), tur = '{callback_query['stage']}' where id = (?);",(admin[0],message.from_user.id))
    conn.execute("update ADMIN set settings = 'add_spare' where id = (?);",(message.from_user.id,))


async def admin_button(message: types.Message, conn, callback_query):
    conn.execute("update ADMIN_ set spare = (?) where id = (?)",(callback_query["name"], message.from_user.id))
    conn.execute("update ADMIN set settings = 'many' where id = (?);",(message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Maxsulot narxini kiriting!")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "Введите цену товара!")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Enter the product price!")



async def admin_many(message: types.Message, conn, language):
    car = conn.execute("select spare from ADMIN_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    admin = conn.execute("select branch from ADMIN where id = (?);",(message.from_user.id,)).fetchall()[0]
    snow = conn.execute("select branches, tur, spare_name from SPARE where number = (?);",(car[0],)).fetchall()
    son = None
    for i in snow[0].split("."):
        if i.split(",")[0] == admin[0]:
            son = 1
            break
    if son is None:
        conn.execute(f"update SPARE set branches = '{snow[0]+'.'+admin[0]+','+message.text}' where number = (?);",(admin[0],))
        conn.execute(f"insert into BRANCH_SPARE(id,turi,spare_name,price,branch) values (?,?,?,?,?);",(car[0],snow[1],snow[2],message.text,admin[0]))
        if language == "uzb":
            await bot.send_message(message.from_user.id,f"Qo'shildi✅")
        elif language == "eng":
            await bot.send_message(message.from_user.id,f"Added✅")
        elif language == "rus":
            await bot.send_message(message.from_user.id,f"Добавлено✅")
    elif son is not None:
        if admin[3] == "uzb":
            await bot.send_message(message.from_user.id, "Siz oldin ham buni qo'shgansiz.")
        elif admin[3] == "rus":
            await bot.send_message(message.from_user.id, "Вы добавили это раньше.")
        elif admin[3] == "eng":
            await bot.send_message(message.from_user.id, "You’ve added this before.")
    conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from branch.menu.main_menu import admin_branch_menu
from branch.product.product_plus import admin_plus_brand
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# async def admin_add_car_corporation(message:types.Message, conn, language, vote_cb):
#     try:
#         await bot.delete_message(message.from_user.id,message.message_id-1)
#     except:
#         pass
#     add = message.text
#     add = add.split(",")
#     conn.execute(f"insert into CAR(corporation,name,number,paditsiya,year) values ('{add[0].strip()}','{add[1].strip()}','{add[2].strip()}','{add[3].strip()}','{add[4].strip()}');")
#     conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
#     if language == "uzb":
#         await bot.send_message(message.from_user.id, "Qabul qilindi✅")
#     elif language == "rus":
#         await bot.send_message(message.from_user.id, "Принятый✅")
#     elif language == "eng":
#         await bot.send_message(message.from_user.id, "Accepted✅")
#     await admin_branch_menu(message,conn,vote_cb,language)
#
#
#
# async def admin_add_car_name(message: types.Message, conn, language, vote_cb):
#     try:
#         await bot.delete_message(message.from_user.id,message.message_id-1)
#     except:
#         pass
#     add = message.text
#     add = add.split(",")
#     admin = conn.execute("select corporation from admin_ where id = (?);",(message.from_user.id,)).fetchall()[0][0]
#     conn.execute(f"insert into CAR(corporation,name,number,paditsiya,year) values ('{admin}','{add[0].strip()}', '{add[1].strip()}', '{add[2].strip()}', '{add[3].strip()}');")
#     conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
#     if language == "uzb":
#         await bot.send_message(message.from_user.id, "Qabul qilindi✅")
#     elif language == "rus":
#         await bot.send_message(message.from_user.id, "Принятый✅")
#     elif language == "eng":
#         await bot.send_message(message.from_user.id, "Accepted✅")
#     await admin_branch_menu(message,conn,vote_cb,language)
#
#
#
# async def admin_add_car_number(message: types.Message, conn, vote_cb, language):
#     try:
#         await bot.delete_message(message.from_user.id,message.message_id-1)
#     except:
#         pass
#     add = message.text
#     add = add.split(",")
#     admin = conn.execute("select corporation, name from admin_ where id = (?);",(message.from_user.id,)).fetchall()[0]
#     conn.execute(f"insert into CAR(name,number,paditsiya,year) values ('{admin[0]}','{admin[1]}','{add[0].strip()}','{add[1].strip()}','{add[2].strip()}');")
#     conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
#     if language == "uzb":
#         await bot.send_message(message.from_user.id, "Qabul qilindi✅")
#     elif language == "rus":
#         await bot.send_message(message.from_user.id, "Принятый✅")
#     elif language == "eng":
#         await bot.send_message(message.from_user.id, "Accepted✅")
#     await admin_branch_menu(message,conn,vote_cb,language)
#
#
# async def admin_add_car_brand(message:types.Message,conn,vote_cb,language):
#     try:
#         await bot.delete_message(message.from_user.id,message.message_id-1)
#     except:
#         pass
#     add = message.text
#     add = add.split(",")
#     admin = conn.execute("select corporation, name, number from admin_ where id = (?);",(message.from_user.id,)).fetchall()[0]
#     conn.execute(f"insert into CAR(name,number,paditsiya,year) values ('{admin[4].strip()}','{admin[5].strip()}','{add[0].strip()}','{add[1].strip()}');")
#     conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
#     if language == "uzb":
#         await bot.send_message(message.from_user.id, "Qabul qilindi✅")
#     elif language == "rus":
#         await bot.send_message(message.from_user.id, "Принятый✅")
#     elif language == "eng":
#         await bot.send_message(message.from_user.id, "Accepted✅")
#     await admin_branch_menu(message,conn,vote_cb,language)

async def admin_add_car_year(message:types.Message,conn,vote_cb,language):
    add = message.text
    admin = conn.execute("select corporation, name, number, paditsiya from admin_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    conn.execute(f"insert into CAR(corporation,name,number,paditsiya,year) values ({admin[0]},'{admin[1].strip()}','{admin[2].strip()}','{admin[3].strip()}','{add.strip()}');")
    conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
    if language == "uzb":
        await bot.send_message(message.from_user.id, "Qabul qilindi✅")
    elif language == "rus":
        await bot.send_message(message.from_user.id, "Принятый✅")
    elif language == "eng":
        await bot.send_message(message.from_user.id, "Accepted✅")
    await admin_branch_menu(message,conn,vote_cb,language)
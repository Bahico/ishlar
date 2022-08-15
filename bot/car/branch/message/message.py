from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..menu.main_menu import admin_branch_menu
from ..oil.oil_add import branch_oil_name, branch_oil_many, branch_oil_add_many
from ..product.add import admin_add, admin_many
from ..product.new.code_new_name import admin_add_car_year
from ..product.new.new_name import admin_new_number, admin_new_brand, admin_new_year
from ..settings.edit_name.edit_name import admin_edit_branch

from config import TOKEN

# some code


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def branch_message(message: types.Message, conn, vote_cb):
    """
    Filial directorining barcha message lari shu yerga kelib o'z turiga kora bo'linadi
    :param message: userning malumotlari
    :param conn: database bilan aloqa
    :param vote_cb: inline keyboard button
    :return: o'zini turiga kora funksiyalarga bo'lib beradi
    """
    admin = conn.execute("select settings, branch, test, language, number from ADMIN where id = (?);", (message.from_user.id,)).fetchall()
    admin = admin[0]
    if admin[3] == "uzb":
        if admin[0] == "login":
            son = 0
            await bot.delete_message(message.from_user.id,message.message_id-1)
            branch = conn.execute("select login, code, id from BRANCH;").fetchall()
            for i in branch:
                if i[0] == message.text:
                    conn.execute("update ADMIN set branch = (?), settings = 'code' where id = (?);",(i[2], message.from_user.id))
                    await bot.send_message(message.from_user.id, "Kodingizni kiriting:")
                    son = 1
                    break
            if son != 1:
                await bot.send_message(message.from_user.id,"Iltimos tog'ri kiriting!\nAdashgan bo'lsangiz menudagi /logout tugmasini bosing iltimos.")

        elif admin[0] == "code":
            try:
                await bot.delete_message(message.from_user.id,message.message_id-1)
            except:
                pass
            branch = conn.execute(f"select login, code, id, admin from BRANCH where id = '{admin[1]}';").fetchall()[0]
            if admin[2] != 1:
                if branch[1] == message.text:
                    conn.execute("update ADMIN set settings = '0', test = 4 where id = (?);", (message.from_user.id,))
                    await bot.send_message(message.from_user.id, "✅Qabul qilindi!\n\nBotdan foydalanish uchun chatga 👉🏻👉🏻/menu deb yozing\n\nIltimos menu dan o'z filialingizni turgan joyini kiritib qo'ying yo'qsa filialingiz ro'yxatdan chiqmaydi.")
                    await admin_branch_menu(message, conn, vote_cb,admin[3])
                    if branch[3] is None:
                        conn.execute(f"update BRANCH set admin = '{str(admin[4])}' where id = (?);",(admin[1],))
                    else:
                        conn.execute(f"update BRANCH set admin = '{str(branch[3])+'.'+str(admin[4])}' where id = (?);",(admin[1],))
                else:
                    await bot.send_message(message.from_user.id, "❌Notog'ri!")
                    conn.execute("update ADMIN set test = 1 where id = (?);", (message.from_user.id,))

        elif admin[0] == "add_name":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                await admin_new_number(message,conn,vote_cb,admin[3],True)
            except:
                await bot.send_message(message.from_user.id,"Nom qo'shishda xatolik bor❌")

        elif admin[0] == "add_number":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            # try:
            await admin_new_brand(message, conn, vote_cb, admin[3],True)
            # except:
            #     await bot.send_message(message.from_user.id,"Number qo'shishda xatolik bor❌")

        elif admin[0] == "add_brand":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                await admin_new_year(message, conn, vote_cb, admin[3],True)
            except:
                await bot.send_message(message.from_user.id,"brand qo'shishda xatolik bor❌")

        elif admin[0] == "add_year":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            # try:
                #int(message.text)
            await admin_add_car_year(message,conn,vote_cb, admin[3])
            # except:
            #     conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
            #     await bot.send_message(message.from_user.id,"Iltimos botdan to'gri foydalaning❌")

        elif admin[0] == "add_spare":
            try:await bot.delete_message(message.from_user.id,message.message_id-1)
            except: pass
            try:
                add = message.text
                add = add.split(",")
                int(add[1])
                if len(add) == 2:
                        await admin_add(message,conn,admin)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Iltimos botdan to'gri foydalaning❌")

        elif admin[0] == "many":
            try:await bot.delete_message(message.from_user.id,message.message_id-1)
            except: pass
            try:
                int(message.text)
                await admin_many(message,conn,admin)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Iltimos botdan to'gri foydalaning❌")

        elif admin[0] == "del":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                int(message.text)
                pass# await admin_del(message, conn, admin[0])
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Iltimos botdan to'gri foydalaning❌")

        elif admin[0] == "edit_name":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            await admin_edit_branch(message, conn, admin)

        elif admin[0] == "add oil":
            await branch_oil_name(message,conn,admin)

        elif admin[0] == "oil many":
            await branch_oil_many(message, conn, vote_cb, admin)

        elif admin[0] == "add oil many":
            await branch_oil_add_many(message,conn,vote_cb,admin)




    #  -------------------------------------------RUS MESSAGE--------------------------
    elif admin[3] == "rus":
        if admin[0] == "login":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            son = 0
            await bot.delete_message(message.from_user.id,message.message_id-1)
            branch = conn.execute("select login, code, id from BRANCH;").fetchall()
            for i in branch:
                if i[0] == message.text:
                    conn.execute("update ADMIN set branch = (?), settings = 'code' where id = (?);",(i[2], message.from_user.id))
                    await bot.send_message(message.from_user.id, "Введите ваш код:")
                    son = 1
                    break
            if son != 1:
                await bot.send_message(message.from_user.id,
                                       "Пожалуйста, введите правильно!\nЕсли вы заблудились, пожалуйста, нажмите кнопку /logout в меню.")

        elif admin[0] == "code":
            try:
                await bot.delete_message(message.from_user.id,message.message_id-1)
            except:
                pass
            branch = conn.execute(f"select login, code, id from BRANCH where login = '{admin[1]}';").fetchall()[0]
            if admin[2] != 1:
                if branch[1] == message.text:
                    conn.execute("update ADMIN set settings = '0', test = 4 where id = (?);", (message.from_user.id,))
                    await bot.send_message(message.from_user.id, "✅Принятый\n\nЧтобы воспользоваться ботом, наберите 👉🏻👉🏻/menu в чате\n\nПожалуйста, введите местоположение вашего филиала из меню, иначе ваш филиал не будет зарегистрирован.")
                    await admin_branch_menu(message, conn, vote_cb,admin[3])
                    if branch[3] is None:
                        conn.execute(f"update BRANCH set admin = '{admin[4]}' where login = (?);",(admin[1]))
                    else:
                        conn.execute(f"update BRANCH set admin = '{branch[3]+'.'+admin[4]}' where login = (?);",(admin[4],admin[1]))
                else:
                    await bot.send_message(message.from_user.id, "❌Неправильно!")
                    conn.execute("update ADMIN set test = 1 where id = (?);", (message.from_user.id,))
            else:
                conn.execute("delete from ADMIN where id = (?);", (message.from_user.id,))
                await bot.send_message(message.from_user.id, "Пожалуйста, используйте бота правильно❌")

        elif admin[0] == "add_name":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                await admin_new_number(message,conn,vote_cb,admin[3],True)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Пожалуйста, используйте бота правильно❌")

        elif admin[0] == "add_number":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:

                await admin_new_brand(message, conn, vote_cb, admin[3], True)

            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Пожалуйста, используйте бота правильно❌")

        elif admin[0] == "add_brand":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                await admin_new_year(message, conn, vote_cb, admin[3],True)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Пожалуйста, используйте бота правильно❌")

        elif admin[0] == "add_year":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                int(message.text)
                await admin_add_car_year(message,conn,vote_cb, admin[3])
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Пожалуйста, используйте бота правильно❌")

        elif admin[0] == "add_spare":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                add = message.text
                add = add.split(",")
                int(add[1])
                if len(add) == 2:
                    await admin_add(message,conn,admin)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Пожалуйста, используйте бота правильно❌")

        elif admin[0] == "many":
            try:await bot.delete_message(message.from_user.id,message.message_id-1)
            except: pass
            try:
                int(message.text)
                await admin_many(message,conn,admin[3])
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Пожалуйста, используйте бота правильно❌")

        elif admin[0] == "del":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                int(message.text)
                # await admin_del(message, conn, admin)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Пожалуйста, используйте бота правильно❌")

        elif admin[0] == "edit_name":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            await admin_edit_branch(message, conn, admin)


        elif admin[0] == "add oil":
            await branch_oil_name(message,conn,admin)

        elif admin[0] == "oil many":
            await branch_oil_many(message, conn, vote_cb, admin)

        elif admin[0] == "add oil many":
            await branch_oil_add_many(message,conn,vote_cb,admin)




    #   -----------------------------------ENG MESSAGE-------------------------------------
    elif admin[3] == "eng":
        if admin[0] == "login":
            son = 0
            try:
                await bot.delete_message(message.from_user.id,message.message_id-1)
            except:
                pass
            branch = conn.execute("select login, code, id from BRANCH;").fetchall()
            for i in branch:
                if i[0] == message.text:
                    conn.execute("update ADMIN set branch = (?), settings = 'code' where id = (?);",(i[2], message.from_user.id))
                    await bot.send_message(message.from_user.id, "Enter your code:")
                    son = 1
                    break
            if son != 1:
                await bot.send_message(message.from_user.id,"Please enter correctly!\nIf you are lost, please click the /logout button in the menu.")

        elif admin[0] == "code":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            branch = conn.execute(f"select login, code, id from BRANCH where login = '{admin[1]}';").fetchall()[0]
            if admin[2] != 1:
                if branch[1] == message.text:
                    conn.execute("update ADMIN set settings = '0', test = 4 where id = (?);", (message.from_user.id,))
                    await bot.send_message(message.from_user.id, "✅Accepted!\n\nTo use the bot, type 👉🏻👉🏻 /menu in the chat\n\nPlease enter the location of your branch from the menu or your branch will not be registered.")
                    await admin_branch_menu(message, conn, vote_cb,admin[3])
                    if branch[3] is None:
                        conn.execute(f"update BRANCH set admin = '{admin[4]}' where login = (?);",(admin[1]))
                    else:
                        conn.execute(f"update BRANCH set admin = '{branch[3]+'.'+admin[4]}' where login = (?);",(admin[4],admin[1]))
                else:
                    await bot.send_message(message.from_user.id, "❌Error!")
                    conn.execute("update ADMIN set test = 1 where id = (?);", (message.from_user.id,))
            else:
                conn.execute("delete from ADMIN where id = (?);", (message.from_user.id,))
                await bot.send_message(message.from_user.id, "Please use the bot correctly❌")

        elif admin[0] == "add_name":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                await admin_new_number(message,conn,vote_cb,admin[3],True)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Please use the bot correctly❌")

        elif admin[0] == "add_number":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:

                await admin_new_brand(message, conn, vote_cb, admin[3], True)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Please use the bot correctly❌")

        elif admin[0] == "add_brand":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:

                await admin_new_year(message, conn, vote_cb, admin[3],True)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Please use the bot correctly❌")

        elif admin[0] == "add_year":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                int(message.text)
                await admin_add_car_year(message,conn,vote_cb, admin[3])
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Please use the bot correctly❌")

        elif admin[0] == "add_spare":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                add = message.text
                add = add.split(",")
                int(add[1])
                if len(add) == 2:
                    await admin_add(message,conn,admin)
                else:
                    conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                    await bot.send_message(message.from_user.id,"Please use the bot correctly❌")
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Please use the bot correctly❌")

        elif admin[0] == "many":
            try:await bot.delete_message(message.from_user.id,message.message_id-1)
            except: pass
            try:
                int(message.text)
                await admin_many(message,conn,admin[3])
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Please use the bot correctly❌")

        elif admin[0] == "del":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            try:
                int(message.text)
                # await admin_del(message, conn, admin)
            except:
                conn.execute("update ADMIN set settings = '0' where id = (?);",(message.from_user.id,))
                await bot.send_message(message.from_user.id,"Please use the bot correctly❌")

        elif admin[0] == "edit_name":
            await bot.delete_message(message.from_user.id,message.message_id-1)
            await admin_edit_branch(message, conn, admin)


        elif admin[0] == "add oil":
            await branch_oil_name(message,conn,admin)

        elif admin[0] == "oil many":
            await branch_oil_many(message, conn, vote_cb, admin)

        elif admin[0] == "add oil many":
            await branch_oil_add_many(message,conn,vote_cb,admin)
import sqlite3

import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from client.basket.basket_main import client_basket
from client.car_arr.car_name import client_car_name
from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_reduce_info(message: types.Message, conn: sqlite3.Connection,
                             vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return:
    """
    client = conn.execute("select longitude, latitude from CLIENT where id = (?);", (message.from_user.id,)).fetchall()[
        0]
    son = 0
    basket = conn.execute("select basket from CLIENT_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    for spare_arr in basket[0].split("."):
        son += 1
        if son == callback_query["name"]:
            spare_arr = spare_arr.split(",")
            spare = conn.execute("select spare_name, branches, id from SPARE where number = (?);",
                                 (int(spare_arr[1]),)).fetchall()[0]
            spare_photo = conn.execute("select photo from PHOTO where id = (?);", (int(spare_arr[1]),)).fetchall()
            branches = []
            for i in spare[1].split("."):
                i = i.split(",")
                branch = \
                    conn.execute("select longitude, latitude, name from BRANCH where admin is not Null and id = (?);",
                                 (int(i[0]),)).fetchall()[0]
                if branch:
                    if client[0] - branch[0] >= 0:
                        longitude = (client[0] - branch[0]) * -1
                    else:
                        longitude = client[0] - branch[0]
                    if client[1] - branch[1] >= 0:
                        latitude = (client[1] - branch[1]) * -1
                    else:
                        latitude = client[1] - branch[1]
                    if longitude + latitude >= 0:
                        location = longitude - latitude
                    else:
                        location = longitude + latitude
                    branches.append([location, branch[2], i[1], int(i[0])])
            for i in branches:
                son = 0
                for branch in branches:
                    if i[0] >= branch[0]:
                        son = 0
                        continue
                    else:
                        son = 1
                        break
                if son == 0:
                    markup = InlineKeyboardMarkup(reply_markup=True)
                    markup.add(
                        InlineKeyboardButton(text="📋Batafsil", callback_data=vote_cb.new(stage="more", id="spare_menu",
                                                                                          name=callback_query["name"],
                                                                                          number=spare_arr[0],
                                                                                          language=callback_query[
                                                                                              "language"],
                                                                                          action="client")),
                        InlineKeyboardButton(text="Yuborish", callback_data=vote_cb.new(stage="send_1", id="spare_menu",
                                                                                        name=callback_query["name"],
                                                                                        number=i[3],
                                                                                        language=callback_query[
                                                                                            "language"],
                                                                                        action="client")),
                        InlineKeyboardButton(text="⬅️ORTGA  ", callback_data=vote_cb.new(stage="start_arr", id="name",
                                                                                         name=callback_query["name"],
                                                                                         number=i[3],
                                                                                         language=callback_query[
                                                                                             "language"],
                                                                                         action="client"))
                    )
                    awa = spare[0] + " nomli maxsulot bor eng yaqin filial \"" + str(
                        i[1]) + "\" bu filialda bu maxsulot " + str(
                        i[2]) + " so'm\n\nAgar hozircha shu maxsulotni o'zi kerak bo'lsa \"Yuborish\" tugmasini bosing"
                    if spare_photo:
                        await bot.send_photo(message.from_user.id, spare_photo[0][0], awa, reply_markup=markup)
                    else:
                        await bot.send_message(message.from_user.id, awa, reply_markup=markup)
                    break
            break


async def client_reduce_add(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
    Tanlagan maxsulotini 1 taga oshiradi
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: basket ni qayta chiqarib beradi
    """
    client = conn.execute("select basket from CLIENT_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    son = 0
    awa = ""
    for spare_arr in client[0].split("."):
        son += 1
        if str(son) == callback_query["name"]:
            spare_arr = spare_arr.split(",")
            add = int(spare_arr[0]) + 1
            if son == 1:
                spare_arr = str(add) + "," + spare_arr[1]
                awa = spare_arr
            else:
                spare_arr = str(add) + "," + spare_arr[1]
                awa += "." + spare_arr
        else:
            if son == 1:
                awa += spare_arr
            else:
                awa += "." + spare_arr
    conn.execute(f"update CLIENT_ set basket = '{awa}' where id = (?);", (message.from_user.id,))
    await client_basket(message, conn, vote_cb, callback_query)


async def client_reduce_reduce(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
    Tanlagan maxsulotini 1 taga kamaytiradi
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: basket ni qayta chiqarib beradi
    """
    client = conn.execute("select basket from CLIENT_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    son = 0
    awa = ""
    for spare_arr in client[0].split("."):
        son += 1
        if str(son) == callback_query["name"]:
            spare_arr = spare_arr.split(",")
            add = int(spare_arr[0]) - 1
            if add <= 0:
                pass
            else:
                spare_arr = str(add) + "," + spare_arr[1]
                if son == 1:
                    awa = spare_arr
                else:
                    awa += "." + spare_arr
        else:
            if son == 1:
                awa += spare_arr
            else:
                awa += "." + spare_arr
    conn.execute(f"update CLIENT_ set basket = '{awa}' where id = (?);", (message.from_user.id,))
    await client_basket(message, conn, vote_cb, callback_query)


async def client_reduce_del(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
    Tanlagan maxsulotni o'chirib tashledi
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: basket ni qayta chiqarib beradi
    """
    client = conn.execute("select basket from CLIENT_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    son = 0
    awa = ""
    for spare_arr in client[0].split("."):
        son += 1
        if str(son) == callback_query["name"]:
            pass
        else:
            if son == 1:
                awa += spare_arr
            else:
                awa += "." + spare_arr
    if awa == "":
        conn.execute("update CLIENT_ set basket = Null where id = (?);", (message.from_user.id,))
    else:
        conn.execute(f"update CLIENT_ set basket = '{awa}' where id = (?);", (message.from_user.id,))
    await client_basket(message, conn, vote_cb, callback_query)


async def client_reduce_remove_all(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
    Client ning olgan barcha extiyot qismlarini o'chirib tashledi
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: bosh menyu chiqarib beradi
    """
    conn.execute("update CLIENT_ set basket = NULL where id = (?);", (message.from_user.id,))
    await client_car_name(message, conn, vote_cb, callback_query["language"])


# async def client_reduce_send(message: types.Message, conn, vote_cb, callback_query):
#     """
#     Olgan maxsulotlarini eng yaqin filiallarga jo'natadi
#     :param callback_query:
#     :param message:
#     :param conn:
#     :param vote_cb:
#     :return: Qaysi filiallarga jo'natganini ko'rsatib bosh menuga qaytarib qo'yadi
#     """
#     pass


async def client_reduce_arrived(message: types.Message, conn: sqlite3.Connection, callback_query: dict):
    client = \
        conn.execute("select spare_branch, received from CLIENT where id = (?);", (message.from_user.id,)).fetchall()[0]
    if client[1] is None:
        conn.execute(f"update CLIENT set received = '{'(' + client[0]}', spare_branch = NULL where id = (?);",
                     (message.from_user.id,))
    elif client[1] is not None:
        conn.execute(
            f"update CLIENT set received = '{client[1] + ')(' + client[0]}', spare_branch = NULL where id = (?);",
            (message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id,
                               "Malumotlar tarixga saqlandi keynchalik ko'rish imkoningiz bor😊\n\nO'z sozlamalaringizni to'girlash uchun chatga 👉🏻👉🏻/menu deb yozing")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id,
                               "Data saved to history, you can see later😊\n\nTo change your settings, chat 👉🏻👉🏻 /menu")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id,
                               "Данные сохранены в историю, можно будет посмотреть позже😊\n\nДля изменения настроек пишите в чат 👉🏻👉🏻 /menu")


async def client_reduce_send1(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    client_ = conn.execute("select basket from CLIENT_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    client = conn.execute("select phone_number, username, latitude, longitude from CLIENT where id = (?);",
                          (message.from_user.id,)).fetchall()[0]
    branch = conn.execute("select admin from BRANCH where id = (?);", (callback_query["number"],)).fetchall()[0]
    son = 0
    basket = ""
    for i in client_[0].split("."):
        son += 1
        if son == callback_query["name"]:
            i = i.split(",")
            spare = conn.execute("select spare_name, tur from SPARE where number = (?);", (int(i[0]),)).fetchall()[0]
            awa = "Buyurtma bor\n\nTuri:" + spare[1] + "\nNomi:" + spare[0] + "\nSoni:" + i[
                1] + "\n\nBuyurtma beruvchi telefon raqami: +" + client[0] + "\nUsername:" + client[
                      1] + "\nTurgan joyi:⬇️"
            for admin in branch[0].split("."):
                admin = conn.execute("select id from ADMIN where number = (?);", (int(admin),)).fetchall()[0][0]
                await bot.send_message(admin, awa)
                await bot.send_location(admin, client[2], client[3])
        else:
            if son == 1:
                basket = i
            else:
                basket += "." + i
    if basket == "":
        conn.execute("update CLIENT_ set basket = NULL where id = (?);", (message.from_user.id,))
    else:
        conn.execute("update CLIENT_ set basket = NULL where id = (?);", (message.from_user.id,))
    await bot.send_message(message.from_user.id, "Yuborildi✅")
    await client_basket(message, conn, vote_cb, callback_query)


async def client_reduce_more(message: types.Message, conn, vote_cb, callback_query):
    spare = conn.execute("select id, spare_number, tur from SPARE where number = (?);",
                         (int(callback_query["number"]),)).fetchall()[0]
    car = \
        conn.execute("select corporation, name, number, paditsiya, year from CAR where id = (?);",
                     (spare[0],)).fetchall()[
            0]
    awa = ""

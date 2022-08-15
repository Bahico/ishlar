from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# async def admin_product_minus(message: types.Message, vote_cb, callback_query):
#     """
#     O'chiriladigon maxsulotni turini soraydi
#     :param message: userning malumotlari
#     :param vote_cb: inline keyboard button
#     :param callback_query: inline keyboard button ning malumotlari
#     :return: maxsulotni 3 xil turini ko'rsatadi
#     """
#     if callback_query["language"] == "uzb":
#         markup = InlineKeyboardMarkup(resize_keyboard=True)
#         markup.row(
#             InlineKeyboardButton(text="⚒ Kuzif",
#                                  callback_data=vote_cb.new(stage="kuzif", id="minus", name="None",number="None",language=callback_query["language"], action="branch")),
#             InlineKeyboardButton(text="⚙️ Mator",
#                                  callback_data=vote_cb.new(stage="mator", id="minus", name="None",
#                                                            number="None",
#                                                            language=callback_query["language"], action="branch")),
#             InlineKeyboardButton(text="💈 Tuning",
#                                  callback_data=vote_cb.new(stage="tuning", id="minus", name="None",
#                                                            number="None",
#                                                            language=callback_query["language"], action="branch"))
#         )
#         await bot.send_message(message.from_user.id, "Qanday extiyot qismni o'chirmoqchisiz?", reply_markup=markup)
#     elif callback_query["language"] == "eng":
#         markup = InlineKeyboardMarkup(resize_keyboard=True)
#         markup.row(
#             InlineKeyboardButton(text="⚒ Kuzif",
#                                  callback_data=vote_cb.new(stage="kuzif", id="minus", name="None",
#                                                            number="None",
#                                                            language=callback_query["language"], action="branch")),
#             InlineKeyboardButton(text="⚙️ Motor",
#                                  callback_data=vote_cb.new(stage="mator", id="minus", name="None",
#                                                            number="None",
#                                                            language=callback_query["language"], action="branch")),
#             InlineKeyboardButton(text="💈 Tuning",
#                                  callback_data=vote_cb.new(stage="tuning", id="minus", name="None",
#                                                            number="None",
#                                                            language=callback_query["language"], action="branch"))
#         )
#         await bot.send_message(message.from_user.id, "What spare part do you want to delete?", reply_markup=markup)
#     elif callback_query["language"] == "rus":
#         markup = InlineKeyboardMarkup(resize_keyboard=True)
#         markup.row(
#             InlineKeyboardButton(text="⚒ Кузиф",
#                                  callback_data=vote_cb.new(stage="kuzif", id="minus", name="None",
#                                                            number="None",
#                                                            language=callback_query["language"], action="branch")),
#             InlineKeyboardButton(text="⚙️ Матор",
#                                  callback_data=vote_cb.new(stage="mator", id="minus", name="None",
#                                                            number="None",
#                                                            language=callback_query["language"], action="branch")),
#                 InlineKeyboardButton(text="💈 Тюнинг",
#                                  callback_data=vote_cb.new(stage="tuning", id="minus", name="None",
#                                                            number="None",
#                                                            language=callback_query["language"], action="branch"))
#         )
#         await bot.send_message(message.from_user.id, "Какую запчасть вы хотите удалить?", reply_markup=markup)
#
#
# async def admin_minus_number(message: types.Message, conn, vote_cb, callback_query):
#     """
#     Maxulotlarni o'ziga tartib raqam bilan chiqarib beradi.
#     :param vote_cb: inline keyboard ning yordamchilari
#     :param message: userning malumotlari
#     :param conn: database bilan aloqa
#     :param callback_query: inline keyboard button ning malumotlari
#     :return: maxsulotlarni qaysi mashinaga ekanligini korsatib o'z tartib raqami
#     """
#     admin = conn.execute("select settings, branch, test, language, name, number, paditsiya, tur, spare from ADMIN where id = (?);",(message.from_user.id,)).fetchall()[0]
#     branch = conn.execute(f"select {callback_query['stage']} from BRANCH where id = (?);", (admin[1],)).fetchall()[0]
#     spare_arr = None
#     son = 0
#     awa = ""
#     awa_s = ""
#     if branch[0] is not None:
#         spare_arr = branch[0].split(".")
#     if callback_query["language"] == "uzb":
#         if spare_arr is not None:
#             awa_s = "Hali hech nima qo'shilmagan."
#             awa = "O'chiriladigan extiyot qismini tartib raqamini kiriting\n\nSizda bor extiyot qismlar to'plami.\n\n"
#             for i in spare_arr:
#                 i = i.split(",")[1]
#                 son += 1
#                 spare_conn = conn.execute(f"select name, number, paditsiya, {admin[7]} from CAR where id = (?);",
#                                           (int(i),)).fetchall()
#                 if spare_conn:
#                     spare_conn = spare_conn[0]
#                     awa += str(son) + ". " + spare_conn[0] + " " + spare_conn[1] + " ning " + spare_conn[2] + " ga " + \
#                            spare_conn[3].split("[")[0]
#         else:
#             awa = "Hali hech nima qo'shilmagan"
#             awa_s = "Hali hech nima qo'shilmagan"
#     elif callback_query["language"] == "rus":
#         if spare_arr is not None:
#             awa_s = "Еще ничего не добавлено."
#             awa = "Введите серийный номер снятой запчасти\n\nТеперь у вас есть набор запчастей.\n\n"
#             for i in spare_arr:
#                 i = i.split(",")[1]
#                 son += 1
#                 spare_conn = conn.execute(f"select name, number, paditsiya, {admin[7]} from CAR where id = (?);",
#                                           (int(i),)).fetchall()
#                 if spare_conn:
#                     spare_conn = spare_conn[0]
#                     awa += str(son) + ". " + spare_conn[0] + " " + spare_conn[1] + " из " + spare_conn[2] + " ga " + \
#                            spare_conn[3].split("[")[0]
#         else:
#             awa = "Еще ничего не добавлено."
#             awa_s = "Еще ничего не добавлено."
#     elif callback_query["language"] == "eng":
#         if spare_arr is not None:
#             awa_s = "Nothing added yet."
#             awa = "Enter the serial number of the removed spare\n\nNow you have a set of spare parts.\n\n"
#             for i in spare_arr:
#                 i = i.split(",")[1]
#                 son += 1
#                 spare_conn = conn.execute(f"select name, number, paditsiya, {admin[7]} from CAR where id = (?);",
#                                           (int(i),)).fetchall()
#                 if spare_conn:
#                     spare_conn = spare_conn[0]
#                     awa += str(son) + ". " + spare_conn[0] + " " + spare_conn[1] + " of " + spare_conn[2] + " ga " + \
#                            spare_conn[3].split("[")[0]
#         else:
#             awa_s = "Nothing added yet."
#             awa = "Nothing added yet."
#
#     markup = InlineKeyboardMarkup(resize_keyboard=True)
#     markup.add(
#         InlineKeyboardButton(text="1", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="1",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="2", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="2",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="3", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="3",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="4", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="4",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="5", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="5",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="6", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="6",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="7", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="7",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="8", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="8",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="9", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                  number="9",
#                                                                  language=callback_query["language"], action="branch")),
#         InlineKeyboardButton(text="10", callback_data=vote_cb.new(stage="number", id="minus", name="None",
#                                                                   number="10",
#                                                                   language=callback_query["language"],
#                                                                   action="branch")),
#     )
#     if 10 >= son > 0:
#         await bot.send_message(message.from_user.id, awa, reply_markup=markup)
#     elif son >= 10:
#         await bot.send_message(message.from_user.id, awa)
#     elif son <= 0:
#         await bot.send_message(message.from_user.id,awa_s)
#
#
# async def admin_del(message: types.Message, conn, admin):
#     """
#     spare ni bir yoli o'chirib yuboradi
#     :param message: userning malumotlari
#     :param conn: database bilan aloqa
#     :param admin: adminning malumotlari
#     :return: kelayotgan malumotni o'chirib o'chganligini bildiradi
#     """
#     my_branch = conn.execute(f"select {admin[7]} from BRANCH where id = {admin[1]};").fetchall()[0]
#     son = 0
#     my_branch = my_branch[0].split(".")
#     for i in my_branch:
#         if str(son) == message.text:
#             my_branch.remove(i)
#             son = 1
#             del_spare = conn.execute(f"select {admin[7]} from CAR where id = {int(i)};").fetchall()
#             spare = 0
#             if del_spare:
#                 del_spare = del_spare[0][0].split("[")[1].split(".")
#                 for branch in del_spare:
#                     spare += 1
#                     if branch.split(",")[0] == str(admin[1]):
#                         del_spare.remove(branch)
#                         break
#                 awa = del_spare[0][0].split("[")[0]
#                 sons = 0
#                 for del_spare in del_spare:
#                     if sons == 0:
#                         awa += del_spare
#                     else:
#                         awa += "." + del_spare
#             sons = 0
#             awa = ""
#             for car in my_branch:
#                 if sons == 0:
#                     awa += car
#                     sons = 1
#                 else:
#                     awa += "." + car
#             conn.execute(f"update BRANCH set {admin[7]} = '{awa}' where id = {admin[1]}")
#
#     if son == 1:
#         if admin[3] == "uzb":
#             await bot.send_message(message.from_user.id, "O'chirildi✅")
#         elif admin[3] == "rus":
#             await bot.send_message(message.from_user.id, "Удалено✅")
#         elif admin[3] == "eng":
#             await bot.send_message(message.from_user.id, "Deleted✅")
#     else:
#         if admin[3] == "uzb":
#             await bot.send_message(message.from_user.id, "Notog'ri❌")
#         elif admin[3] == "rus":
#             await bot.send_message(message.from_user.id, "Неправильно❌")
#         elif admin[3] == "eng":
#             await bot.send_message(message.from_user.id, "Wrong❌")
#     conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))

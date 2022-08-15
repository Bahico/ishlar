# from aiogram.dispatcher import Dispatcher
# from aiogram import Bot, types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils import executor
#
# from config import TOKEN
#
# # some code
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start'])
# async def get_start(message:types.Message):
#     await message.answer("Salom!")
#
# @dp.callback_query_handler()
#
# @dp.message_handler()
# async def get_message(message:types.Message):
#     await bot.delete_message(message.from_user.id,message.message_id-1)
#     await message.delete()
#     await message.answer("qale")
#
# if __name__ == '__main__':
#    executor.start_polling(dp, skip_updates=True)

# son1 = -2
# son2 = -5
# if son1-son2 >= 0:
#     print(son1+son2)
#     print(True)
# else:
#     print(False)
#     print(son1+son2)

# arr_ = [[5,2], [5,2], [5,2], [7,2], [5,2], [6,2]]
# for i in arr_:
#     son = 0
#     for arr in arr_:
#         if i[0] >= arr[0]:
#             son = 1
#             continue
#         else:
#             son = 0
#             break
#     if son == 0:
#         continue
#     else:
#         print(i)
#         break
# message = "2008-2012"
#
# son = 0
# sons = 0
# try:
#     for i in message:
#         son += 1
#         if son >= 5:
#             son = 0
#             sons += 1
#         else:
#             int(i)
#     if sons == 1:
#         print("Good!")
#     else:
#         print("Error!!")
# except:
#     print("Error!")
#
# son = 11
#
# if son >= 10:
#     print(True)
# import sqlite3
#
# conn = sqlite3.connect("sqlite.db")
#
# print(conn.execute("select * from ADMIN where id is not Null;").fetchall())


# son = 3
#
# if son % 2 == 0:
#     print(True)
# else:
#     print(False)
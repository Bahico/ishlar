from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from ..food_minus.food_minus import get_food_minus
from ..food_minus.food_arr import get_arr
from ..food_minus.food_delete import get_delete_
from ..food_plus.food_plus import get_food_plus
from ..menu.main_menu import get_admin_menu
from ..product_del.product_del import get_product
from ..product_del.product_delete import get_delete, get_product_del

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_admin_callback(message: types.Message, conn, vote_cb, callback_query):
    branch = conn.execute("select fast_food, waffle, coffee, drinks from BRANCH where id = (?);",(callback_query["branch"],)).fetchall()
    branch = branch[0]
    if callback_query["text"] == "menu":
        if callback_query["location"] == "+":
            await get_food_plus(message,vote_cb,callback_query)
        elif callback_query["location"] == "-":
            await get_food_minus(message,conn,vote_cb,callback_query,branch)
        elif callback_query["location"] == "--":
            await get_product(message,conn,vote_cb)

    if callback_query["location"] == "+":
        if callback_query["text"] == "coffee":
            conn.execute("update ADMIN set plus = (?), bosqich = (?) where id = (?);",("coffee",3,message.from_user.id))
            await bot.send_message(message.from_user.id,"Qo'shadigan coffee nomi nima?\n\nIltimos nomida . , bolmasin!")
        elif callback_query["text"] == "fast_food":
            conn.execute("update ADMIN set plus = (?), bosqich = (?) where id = (?);",("fast_food",3,message.from_user.id))
            await bot.send_message(message.from_user.id,"Qo'shadigan fast food nomi nima?\n\nIltimos nomida . , bolmasin!")
        elif callback_query["text"] == "waffle":
            conn.execute("update ADMIN set plus = (?), bosqich = (?) where id = (?);",("waffle",3,message.from_user.id))
            await bot.send_message(message.from_user.id,"Qo'shadigan vafli nomi nima?\n\nIltimos nomida . , bolmasin!")
        elif callback_query["text"] == "drinks":
            conn.execute("update ADMIN set plus = (?), bosqich = (?) where id = (?);",("drinks",3,message.from_user.id))
            await bot.send_message(message.from_user.id,"Qo'shadigan salqin ichimlik nomi nima?\n\nIltimos nomida . , bolmasin!")
        elif callback_query["text"] == "back":
            await get_admin_menu(message,conn,vote_cb)

    elif callback_query["location"] == "-":
        if callback_query["text"] == "coffee":
            await get_arr(message,conn,vote_cb,callback_query)
        elif callback_query["text"] == "fast_food":
            await get_arr(message,conn,vote_cb,callback_query)
        elif callback_query["text"] == "waffle":
            await get_arr(message,conn,vote_cb,callback_query)
        elif callback_query['text'] == "drinks":
            await get_arr(message,conn,vote_cb,callback_query)

    elif callback_query["location"] == "--":
        if callback_query["text"] == "coffee":
            await get_delete(message,conn,vote_cb,callback_query)
        elif callback_query["text"] == "fast_food":
            await get_delete(message,conn,vote_cb,callback_query)
        elif callback_query["text"] == "waffle":
            await get_delete(message,conn,vote_cb,callback_query)
        elif callback_query['text'] == "drinks":
            await get_delete(message,conn,vote_cb,callback_query)

    elif callback_query["location"] == "coffee":
        if callback_query["language"] != "--":
            await get_delete_(message,conn,vote_cb,callback_query)
        else:
            await get_product_del(message, conn, callback_query)
    elif callback_query["location"] == "fast_food":
        if callback_query["language"] != "--":
            await get_delete_(message,conn,vote_cb,callback_query)
        else:
            await get_product_del(message, conn, callback_query)
    elif callback_query["location"] == "waffle":
        if callback_query["language"] != "--":
            await get_delete_(message,conn,vote_cb,callback_query)
        else:
            await get_product_del(message, conn, callback_query)
    elif callback_query["location"] == "drinks":
        if callback_query["language"] != "--":
            await get_delete_(message,conn,vote_cb,callback_query)
        else:
            await get_product_del(message, conn, callback_query)

    await bot.delete_message(message.from_user.id,message.message.message_id)

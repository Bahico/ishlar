from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from bot_.callback.admin_all import get_admin_all
from bot_.number.admin_number import get_admin_number
from bot_.delete.delete import get_user_del
from ..number.user_number import get_user_number
from ..number.branch import get_number
from ..add_branch.add_branch import get_add_branch
from ..del_branch.del_branch import get_del_branch, get_delete
from ..adit_code.branch import get_edit, get_delivery_food, get_delivery_edit, get_food_edit
from ..communication.communication import get_communication, get_communication_finish


from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_bot_callback(message: types.Message, conn, callback_query, vote_cb):
    if callback_query["location"] == "branch":
        if callback_query["text"] == "+":
            await get_add_branch(message)
        elif callback_query["text"] == "-":
            await get_del_branch(message,conn,vote_cb)
        elif callback_query["text"] == "del":
            await get_delete(message,conn,callback_query["branch"])
        elif callback_query["text"] == "edit":
            await get_delivery_food(message,conn,vote_cb,callback_query["branch"])

    elif callback_query["location"] == "admin":
        if callback_query["text"] == "number":
            await get_admin_number(message, conn, vote_cb)
        elif callback_query["text"] == "communication":
            await get_communication(message,conn,callback_query["branch"],vote_cb)
        elif callback_query["text"] == "delete":
            await get_user_del(message,conn,callback_query["branch"],callback_query["language"],vote_cb)
        elif callback_query["text"] == "phone":
            await bot.send_message(message.from_user.id,"+998"+str(callback_query["branch"]))



    elif callback_query["location"] == "user":
        if callback_query["text"] == "number":
            await get_user_number(message,conn,vote_cb)

    elif callback_query["location"] == "code":
        if callback_query["text"] == "add":
            await get_edit(message,conn,vote_cb)


    elif callback_query["location"] == "branch":
        if callback_query["text"] == "all":
            await get_admin_all(message, conn, vote_cb)
        elif callback_query["text"] == "selection":
            await get_number(message,conn,callback_query["branch"],callback_query["language"],vote_cb)

    elif callback_query["location"] == "client":
        if callback_query["text"] == "communication":
            await get_communication(message,conn,callback_query["branch"],vote_cb)
        elif callback_query["text"] == "delete":
            await get_user_del(message,conn,callback_query["branch"],callback_query["language"],vote_cb)
        elif callback_query["text"] == "phone":
            await bot.send_message(message.from_user.id,"+998"+str(callback_query["branch"]))

    elif callback_query["location"] == "communication":
        if callback_query["text"] == "finish":
            await get_communication_finish(message)

    elif callback_query["location"] == "food":
        if callback_query["text"] == "edit":
            await get_food_edit(message,callback_query["branch"])
    elif callback_query["location"] == "delivery":
        if callback_query["text"] == "edit":
            await get_delivery_edit(message,callback_query["branch"])

    await bot.delete_message(message.from_user.id,message.message.message_id)

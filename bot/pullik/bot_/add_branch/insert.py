from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def get_insert_branch(message: types.Message, conn,branch_food_code,branch_delivery_code,add_branch_name):
    conn.execute("insert into BRANCH(name,food_code,delivery_code,latitude,longitude) values (?,?,?,?,?);",(add_branch_name,branch_food_code,branch_delivery_code,message.location.latitude,message.location.longitude))
    await bot.send_message(message.from_user.id,"Yangi filial yaratildi✅",reply_markup=ReplyKeyboardRemove())
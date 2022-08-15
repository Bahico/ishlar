from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

add_branch_true = None


async def get_add_branch(message: types.Message):
    global add_branch_true
    add_branch_true = True
    await bot.send_message(message.from_user.id, "Filial nomini kiriting.\n\nIltimos nomda \". ,\" lar bo'lmasin.")


def get_none():
    global add_branch_true
    add_branch_true = None

from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentTypes
from aiogram.utils import executor


BOT_TOKEN = '5076362804:AAE5EGEkcF2-Wulbn--qhBOTxSrFX_LLiYA'


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

async def get_start(message: types.Message):
    pass
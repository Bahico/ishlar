# from aiogram.dispatcher import Dispatcher
# from aiogram import Bot, types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils import executor
# from aiogram.utils.callback_data import CallbackData
#
# TOKEN = '5076362804:AAE5EGEkcF2-Wulbn--qhBOTxSrFX_LLiYA'
#
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
# PRICE = types.LabeledPrice(label='Настоящая Машина Времени', amount=100000)
#
# PAYMENTS_PROVIDER_TOKEN = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065'
#
# @dp.message_handler(commands=['buy'])
# async def process_buy_command(message: types.Message):
#     # if PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
#         await bot.send_message(message.chat.id,'pre_buy_demo_alert')
#         await bot.send_invoice(
#             message.chat.id,
#             title='tm_title',
#             description='tm_description',
#             provider_token=PAYMENTS_PROVIDER_TOKEN,
#             currency='UZS',
#             photo_url='https://images.fineartamerica.com/images-medium-large/2-the-time-machine-dmitriy-khristenko.jpg',
#             photo_height=512,  # !=0/None, иначе изображение не покажется
#             photo_width=512,
#             photo_size=512,
#             is_flexible=False,  # True если конечная цена зависит от способа доставки
#             prices=[PRICE],
#             start_parameter='time-machine-example',
#             payload='4242424242424242'
#             )
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentTypes
from aiogram.utils import executor


BOT_TOKEN = '5076362804:AAE5EGEkcF2-Wulbn--qhBOTxSrFX_LLiYA'
PAYMENTS_PROVIDER_TOKEN = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

# Setup prices
prices = [
    types.LabeledPrice(label='Working Time Machine', amount=10000),
    types.LabeledPrice(label='Gift wrapping', amount=10000),
]

# Setup shipping options
shipping_options = [
    types.ShippingOption(id='instant', title='WorldWide Teleporter').add(types.LabeledPrice('Teleporter', 10000)),
    types.ShippingOption(id='pickup', title='Local pickup').add(types.LabeledPrice('Pickup', 30000)),
]


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Hello, I'm the demo merchant bot."
                           " I can sell you a Time Machine."
                           " Use /buy to order one, /terms for Terms and Conditions")


@dp.message_handler(commands=['terms'])
async def cmd_terms(message: types.Message):
    await bot.send_message(message.chat.id,
                           'Thank you for shopping with our demo bot. We hope you like your new time machine!\n'
                           '1. If your time machine was not delivered on time, please rethink your concept of time'
                           ' and try again.\n'
                           '2. If you find that your time machine is not working, kindly contact our future service'
                           ' workshops on Trappist-1e. They will be accessible anywhere between'
                           ' May 2075 and November 4000 C.E.\n'
                           '3. If you would like a refund, kindly apply for one yesterday and we will have sent it'
                           ' to you immediately.')


@dp.message_handler(commands=['buy'])
async def cmd_buy(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Real cards won't work with me, no money will be debited from your account."
                           " Use this test card number to pay for your Time Machine: `4242 4242 4242 4242`"
                           "\n\nThis is your demo invoice:", parse_mode='Markdown')
    await bot.send_invoice(message.chat.id, title='Working Time Machine',
                           description='Want to visit your great-great-great-grandparents?'
                                       ' Make a fortune at the races?'
                                       ' Shake hands with Hammurabi and take a stroll in the Hanging Gardens?'
                                       ' Order our Working Time Machine today!',
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='UZS',
                           photo_url='https://telegra.ph/file/d08ff863531f10bf2ea4b.jpg',
                           photo_height=512,  # !=0/None or picture won't be shown
                           photo_width=512,
                           photo_size=512,
                           is_flexible=False,  # True If you need to set up Shipping Fee
                           prices=prices,
                           start_parameter='time-machine-example',
                           payload='4242424242424242')



@dp.shipping_query_handler(lambda query: True)
async def shipping(shipping_query: types.ShippingQuery):
    await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                                    error_message='Oh, seems like our Dog couriers are having a lunch right now.'
                                                  ' Try again later!')


@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                        error_message="Aliens tried to steal your card's CVV,"
                                                      " but we successfully protected your credentials,"
                                                      " try to pay again in a few minutes, we need a small rest.")


@dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(message: types.Message):
    await bot.send_message(message.chat.id,
                           'Hoooooray! Thanks for payment! We will proceed your order for `{} {}`'
                           ' as fast as possible! Stay in touch.'
                           '\n\nUse /buy again to get a Time Machine for your friend!'.format(
                               message.successful_payment.total_amount / 100, message.successful_payment.currency),
                           parse_mode='Markdown')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
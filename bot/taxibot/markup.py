from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# btnMain = KeyboardButton('Asosiy Menu')




# btnInfo = KeyboardButton("Ro'yxatdan o'tish")
# btnPeople = KeyboardButton('odam olish')
# btnReservation = KeyboardButton('Joy band qilish')
# btnCar = KeyboardButton('Bor mashinalar')

btnToday = KeyboardButton("Today")
btnDate = KeyboardButton("Date")

#  ---Other Menu---

# mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnCar, btnPeople, btnReservation)


#  ---visible to registered passengers----

# otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnReservation, btnCar)


# btnPessanger = KeyboardButton('Yolovchi')
# btnDrive = KeyboardButton('Haydovchi')
# registrationMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDrive,btnPessanger)

#  ---Registration menu---

btnNumber = KeyboardButton('Telefon nomer',request_contact=True)
btnLocation = KeyboardButton('Turgan joy',request_location=True)
btnNext = KeyboardButton('Taksi chaqirish')
tlgNumber = KeyboardButton('Shu telelgram nomeri',request_contact=True)
createNumber = KeyboardButton("O'zim nomer kiritaman")
back = KeyboardButton('Orqaga')
order = KeyboardButton("Buyurtmalar")
# btnTime = KeyboardButton('Vaqtni kiriting')
# btnCarNumber = KeyboardButton('Mashina raqami')


#  ---Registration section---

AdminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnToday,btnDate,order)
PessangerMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnNumber)
backMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(back)
PessangerCreateNumber = ReplyKeyboardMarkup(resize_keyboard=True).add(tlgNumber,createNumber)
PessangerMenu2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnLocation)
NextMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnNext)


#  ---Drive Registration---

# DriveMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnNumber,btnCarNumber, btnMain)
#
# SimpleMenu = ReplyKeyboardMarkup(resize_keyboard=False)

#  ---Date Menu---
start_kb = ReplyKeyboardMarkup(resize_keyboard=True,)
start_kb.row('Navigation Calendar','Dialog Calendar')
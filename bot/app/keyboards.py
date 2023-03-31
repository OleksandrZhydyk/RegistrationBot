from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


inline_button_signup = KeyboardButton("SignUp", callback_data='True')
reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reply_kb.add(inline_button_signup)



import io
from aiogram import types
from aiogram.dispatcher import FSMContext
from app import dp, bot
from . checkers import check_username, check_password
from . import messages, send_data, keyboards
from . states import AuthStates
from . config import conf_bot


@dp.message_handler(commands=['start'], state="*")
async def helper(message: types.Message):
    await AuthStates.start_register.set()
    await message.answer(messages.WELLCOME_REGISTER, reply_markup=keyboards.reply_kb)


@dp.message_handler(state=AuthStates.start_register)
async def signup_start(message: types.Message, state: FSMContext):
    if message.text == "SignUp":
        res = await send_data.check_user_exists(message.from_user.id)
        async with state.proxy() as data:
            data.update(res)
        if res['user_exist']:
            await message.answer("You are already registered")
            await state.reset_state(with_data=False)
        else:
            await AuthStates.next()
            await message.answer(messages.USERNAME_NOTICE)


@dp.message_handler(state=AuthStates.username)
async def get_username(message: types.Message, state: FSMContext):
    if message.text:
        if not check_username(message.text):
            return await message.answer(messages.USERNAME_ADVISE)
        res = await send_data.check_username_exists(message.text)
        if res['username_exist']:
            return await message.answer("This username already exists, please choose another")
        else:
            async with state.proxy() as data:
                data.update({'username': message.text})
            await AuthStates.next()
            return await message.answer(messages.PASSWORD_NOTICE)


@dp.message_handler(state=AuthStates.password)
async def get_password(message: types.Message, state: FSMContext):
    if message.text:
        async with state.proxy() as data:
            username = data['username']
            if not check_password(message.text, username):
                return await message.answer(messages.PASSWORD_ADVISE)
            data.update({'password': message.text})
        await AuthStates.next()
        await message.answer("Please confirm the password")


async def get_user_photo(user_id: int):
    user_profile_photo = await bot.get_user_profile_photos(user_id)
    if len(user_profile_photo.photos) > 0:
        file = await bot.get_file(user_profile_photo.photos[0][0].file_id)
        result: io.BytesIO = await bot.download_file(file.file_path)
        return result
    return False


async def registration(message: types.Message, data: dict):
    username = data['username']
    password = data['password']
    confirmed_password = data['confirmed_password']
    res = await send_data.registration(username, password, confirmed_password)
    if res['registration']:
        user_data = {
                     't_user_id': message.from_user.id,
                     't_first_name': message.from_user.first_name,
                     't_username': message.from_user.get('username', "No username"),
                     }
        photo_obj = await get_user_photo(message.from_user.id)
        res = await send_data.fill_profile(username, user_data, photo_obj)
        if res['profile_update']:
            return True
        return "Profile was not created"
    return "Registration error"


@dp.message_handler(state=AuthStates.confirm_password)
async def get_password_confirmation(message: types.Message, state: FSMContext):
    if message.text:
        async with state.proxy() as data:
            if data['password'] == message.text:
                data['confirmed_password'] = message.text
                await message.answer("Please wait ...")
                res = await registration(message, data)
                await state.finish()
                if res is True:
                    keyboard = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton('Login',
                                                        url=f"{conf_bot.HOST}/login")
                    keyboard.add(button)
                    return await message.answer("Click button to login", reply_markup=keyboard)
                return await message.answer(res)
            return await message.answer("Confirmation password doesn't equal the password")


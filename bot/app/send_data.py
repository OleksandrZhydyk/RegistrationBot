import aiohttp

from aiohttp import FormData

from . config import conf_bot


async def register():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{conf_bot.BACKEND_HOST}/register/") as response:
            if response.status == 200:
                return await response.json()
            return None


async def check_user_exists(t_user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{conf_bot.BACKEND_HOST}/user_exist/{t_user_id}") as response:
            if response.status == 200:
                return await response.json()
            return None


async def check_username_exists(username):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{conf_bot.BACKEND_HOST}/username_exist/{username}") as response:
            if response.status == 200:
                return await response.json()
            return None


async def registration(username: str, password: str, confirmed_password: str):
    async with aiohttp.ClientSession() as session:
        data = {'username': username, 'password1': password, 'password2': confirmed_password}
        async with session.post(f"{conf_bot.BACKEND_HOST}/register", json=data) as response:
            if response.status == 200:
                return await response.json()
            return None


async def fill_profile(username: str, user_data: dict, photo_obj):
    data = FormData()
    data.add_field('t_user_id', str(user_data['t_user_id']), content_type='multipart/form-data')
    data.add_field('t_username', user_data['t_username'], content_type='multipart/form-data')
    if photo_obj:
        data.add_field('photo', photo_obj, filename=f'{user_data["t_user_id"]}.png', content_type='multipart/form-data')

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{conf_bot.BACKEND_HOST}/update_profile/{username}", data=data) as response:
            if response.status != 200:
                return None
            return await response.json()

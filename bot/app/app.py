from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from . config import conf_bot


bot = Bot(token=conf_bot.BOT_ACCESS_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

import logging
from typing import Union

from aiogram import Bot, Dispatcher, types

from noio.bot import dialog
from noio.models import User
from settings import BOT_API_TOKEN

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)
logger = logging.getLogger(__name__)


def _init_user(message: Union[types.Message, types.CallbackQuery]):
    return {"name": message.from_user.first_name, "telegram_id": message.from_user.id}


@dp.message_handler(commands=["start", "help"])
async def handle_welcome(message: types.Message):
    user = User.get_or_create(**_init_user(message))

    await message.reply(
        dialog.welcome.format(name=user.name),
        reply=False,
    )


@dp.callback_query_handler(lambda c: c.data == "start")
async def handle_welcome_inline(callback_query: types.CallbackQuery):
    user = User.get_or_create(**_init_user(callback_query))

    await bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=dialog.welcome.format(name=user.name),
    )

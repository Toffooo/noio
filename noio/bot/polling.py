from noio.bot.service import bot
from noio.models import Notice, User


async def send_message():
    notices = Notice.filter(is_new=True)
    telegram_ids = [user.telegram_id for user in User.all()]

    for telegram_id in telegram_ids:
        for notice in notices:
            notice.is_new = False
            await bot.send_message(
                text=f"{notice.name} \n{notice.link}", chat_id=telegram_id
            )
            notice.save()

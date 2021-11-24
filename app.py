import logging

from loader import db


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)
    logging.info("Create a database connection")
    await db.create()
    logging.info("Create a table of person")
    await db.create_table_person()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)

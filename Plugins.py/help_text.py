
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        disable_web_page_preview=False,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        disable_web_page_preview=False,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgrade(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

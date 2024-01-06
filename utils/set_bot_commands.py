from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("photo", "picture"),
            types.BotCommand("video", "little video"),
            types.BotCommand("album", "album "),
        ]
    )

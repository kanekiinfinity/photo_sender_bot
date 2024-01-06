from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, ContentType

from loader import dp, bot

@dp.message_handler(content_types=ContentType.PHOTO)
async def getfileidPhoto(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=ContentType.VIDEO)
async def get_file_idv(message: types.Message):
    await message.reply(message.video.file_id)

@dp.message_handler(Command('photo'))
async def send_photo(message: types.Message):
    photo_id = "AgACAgIAAxkBAAMMZZlDSF3HAvsxdQIk8asH7UrrcNAAAtDcMRv3BclI0vrz0F0TrcABAAMCAANtAAM0BA"
    await message.reply_photo(photo_id, caption="Rasm")

@dp.message_handler(Command('video'))
async def send_video(message: types.Message):
    video_id = "BAACAgIAAxkBAAMOZZlDWpCwheh-isLvOvdvlqZmSY8AAi49AAL3BclIqRn-YGMCUZA0BA"
    await message.reply_video(video_id, caption="Video")

@dp.message_handler(Command('album'))
async def send_albom(message: types.Message):
    album = types.MediaGroup()
    photo_id = "AgACAgIAAxkBAAMMZZlDSF3HAvsxdQIk8asH7UrrcNAAAtDcMRv3BclI0vrz0F0TrcABAAMCAANtAAM0BA"
    photo1 = "AgACAgIAAxkBAAMWZZlFWUuTKEIkl9B9dkf7eVHJo_kAAtzcMRv3BclIKa-7QPkoqF4BAAMCAANtAAM0BA"
    video_id = "BAACAgIAAxkBAAMOZZlDWpCwheh-isLvOvdvlqZmSY8AAi49AAL3BclIqRn-YGMCUZA0BA"
    album.attach_photo(photo=photo_id)
    album.attach_photo(photo=photo1)
    album.attach_video(video=video_id)
    await message.reply_media_group(media=album)


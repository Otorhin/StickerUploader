import telebot
import os
"""
Можно включить прокси, если ты из РФ
from telebot import apihelper
apihelper.proxy = {'https': 'http://username:password@ip:host'}
"""

token = '11111:abaaba'  # Токен вашего бота
tg_user_id = 11111  # Ваш TG ID. Можно узнать в @myidbot
url_pack = 'the_best_stickers'  # Часть ссылки на стикеры. Только англ. символы и цифры
name_pack = 'The Best Stickers'  # Название вашего стикер пака
emoji = '🥰🤖🐰'  # Emoji которые проставятся на все стикеры
folder = 'C:\\Users\\User\\Desktop\\1s\\'  # Папка из которой берутся стикеры


bot = telebot.TeleBot(token=token)
url_pack += '_by_' + bot.get_me().username

i = 1

for f in os.listdir(folder):
    sticker = open(f'{folder}{f}', 'rb')
    try:
        if i == 1:
            bot.create_new_sticker_set(tg_user_id, url_pack, name_pack, sticker, emoji)
            bot.send_message(tg_user_id, f'Create sticker pack t.me/addstickers/{url_pack}')
        else:
            bot.add_sticker_to_set(tg_user_id, url_pack, sticker, emoji)
        i += 1
    except Exception as e:
        _ = f'Возникла ошибка: <code>{e}</code>\n\nВозможно файл {folder}{f} больше 512 КБ.'
        bot.send_message(tg_user_id, _)

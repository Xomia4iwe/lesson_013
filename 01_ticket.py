# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse


def make_ticket(fio, from_, to, date, save=False):
    im = Image.open('images/ticket_template.png')
    size = 15
    font = ImageFont.truetype("ofont.ru_FreeSet.ttf", size=size)
    im_txt = ImageDraw.Draw(im)
    im_txt.text((45, 142-size), fio, font=font, fill=ImageColor.colormap['black'])
    im_txt.text((45, 212-size), from_, font=font, fill=ImageColor.colormap['black'])
    im_txt.text((45, 278-size), to, font=font, fill=ImageColor.colormap['black'])
    im_txt.text((285, 278-size), date, font=font, fill=ImageColor.colormap['black'])
    if save == True:
        out_path = str(fio.replace('.', '')) + '.png'
        im.save(out_path)


passenger = 'Иванов Иван'
departure = 'Земля'
arrival = 'Луна'
data = '09.12'

make_ticket(passenger, departure, arrival, data, save=True)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

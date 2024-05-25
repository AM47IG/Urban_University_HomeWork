# -*- coding: utf-8 -*-

import csv
from pprint import pprint


def write_holiday_cities(first_letter='L'):
    info_list = ['Посетили', 'Хотят посетить', 'Никогда не были в', 'Следующим городом будет']
    have = set()
    want = set()
    with open('travel-notes.csv', 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0].upper().startswith(first_letter.upper()):
                have.update(row[1].split(';'))
                want.update(row[2].split(';'))
    not_has = sorted(want - have)
    go_to = [not_has[0], ]
    have = sorted(have)
    want = sorted(want)
    with open('holiday.csv', 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        for list_ in (have, want, not_has, go_to):
            writer.writerow(list_)
        # writer = csv.writer(out_file, delimiter=':')
        # for info, list_ in zip(info_list, (have, want, not_has, go_to)):
        #     writer.writerow([info] + [';'.join(list_)])


write_holiday_cities(input('Введите первую букву имени: '))


'''
Посетили: Aktau, Beijing, Dushanbe, Irkutsk, Kiev, Luxembourg, Minsk, Moscow, New York, Saint Petersburg, Tbilisi, Vladikavkaz
Хотят посетить: Almaty, Cairo, Kursk, Levan, Minsk, Nizhny Tagil, Orel, Tokyo
Никогда не были в: Almaty, Cairo, Kursk
Следующим городом будет: Almaty
'''
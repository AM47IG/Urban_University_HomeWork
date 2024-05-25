# -*- coding: utf-8 -*-
import json


def employees_rewrite(sort_type):
    with open('employees.json', mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    for k in data['employees'][0]:
        if k.lower() == sort_type.lower():
            valid_sort_type = k
            break
    else:
        raise ValueError('Bad key for sorting')
    sort_data = sorted(data['employees'], key=lambda x: x[valid_sort_type])
    with open(f'employees_{sort_type.lower()}_sorted.json', mode='w+', encoding='utf-8') as out_file:
        json.dump(sort_data, out_file, indent=4)


employees_rewrite('department')

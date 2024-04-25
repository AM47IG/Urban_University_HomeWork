# Для запуска кода необходимо выделить весь код и раскомментировать...

from pprint import pprint
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# С помощью библиотеки requests получил состав Сникерса с API Spoonacular
# Эта библиотека позволяет не тратить время на составление
# правильных запросов и обработки ответа от сервера.
# Возможностей много, как и в остальных представленных
# библиотеках.
print(f'{'requests':*^30}')
response = requests.get('https://api.spoonacular.com/food/products/22347',
                        params={'apiKey': '92ff0441402543658ecf622434a7e5ef'})
ingredient_list = response.json()['ingredientList']
print('requests: Состав Сникерса >>>')
pprint(ingredient_list)
print()


# С помощью библиотеки pandas можно быстро работать с DataFrame,
# создавать, конвертировать, анализировать, составлять диаграммы и многое другое.
# В данном примере прочитали данные из файла CSV, проанализировали,
# узнали статистику и записали файл в таблицу Excel.
print(f'{'pandas':*^30}')
students = pd.read_csv("StudentsPerformance.csv")
# print(students.head())
# print(students.tail(3))
print(students.groupby(["gender", "test preparation course"])["writing score"].count())
# students.to_excel("students.xlsx")
print()


# С помощью библиотеки matplotlib построили график на основе данных из предыдущей библиотеки.
plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()


# С помощью библиотеки numpy производится эффективная работа с матрицами.
# В примере ниже парой строчек создается две матрицы и операция над ними.
print(f'{'numpy':*^30}')
a1 = np.arange(1, 26).reshape(5, 5)
a2 = np.transpose(a1)
print(a1)
print(a2)
a3 = a1 - a2
print(a3)
print()


# Библиотека pillow позволяет работать с изображения (читать, редактировать, показывать, конвертировать).
# В примере я зашакалил изображение, перевел в чб и сохранил в формате PNG
image = Image.open('ED.jpg')
width, height = image.size
new_width = 100  # ширина
new_height = int(new_width * height / width)
image = image.resize((new_width, new_height))
grayscale = image.convert('L')
grayscale.show()
grayscale.save('grayscale.png', 'PNG')

# ИТОГ: Библиотеки в Python представляют неограниченные возможности по облегчению работы
# над кодом. Очень важно уметь находить необходимые библиотеки, читать документацию, следить за обновлениями
# и новыми функциями. Так же важно понимать какие конкретно библиотеки подходят для конкретных проектов.
# Голова может закружиться от их обилия. Так же думаю, что нужно понимать какие конкретные возможности использовать
# из определенной библиотеки, так как зачастую эти возможности с излишком перекрывают потребности.

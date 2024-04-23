from pprint import pprint
import requests
# import pandas
# import numpy
# import matplotlib
# import pillow


#  С помощью библиотеки requests получил состав Сникерса
response = requests.get('https://api.spoonacular.com/food/products/22347',
                        params={'apiKey': '92ff0441402543658ecf622434a7e5ef'})
ingredient_list = response.json()['ingredientList']
print('requests: Состав Сникерса >>>')
pprint(ingredient_list)
print()
#  С помощью библиотеки requests получил состав Сникерса

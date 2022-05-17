"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""



def main(product_list):
	all_items_sold = []

	for product in product_list:
		print(f"Cуммарное количество продаж {product['product']} - {sum(product['items_sold'])}")
		print(f"Среднее количество продаж {product['product']} - {round(sum(product['items_sold']) / len(product['items_sold']))}")
		all_items_sold += product['items_sold']

	print(f"Cуммарное количество продаж всех товаров - {sum(all_items_sold)}")
	print(f"Среднее количество продаж всех товаров - {round(sum(all_items_sold) / len(all_items_sold))}")

product_list = [
	{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
	]

    
if __name__ == "__main__":
    main(product_list)

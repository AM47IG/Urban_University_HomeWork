from multiprocessing import Pool, Manager


class WarehouseManager:

    def __init__(self):
        self.data = Manager().dict()

    def process_request(self, request):
        product, operation, amount = request
        if operation == "receipt":
            self.data[product] = self.data.get(product, 0) + amount
            print(f'Склад: {product} увеличено на {amount}')
        elif operation == "shipment" and self.data.get(product, False) and self.data[product] >= amount:
            self.data[product] -= amount
            print(f'Склад: {product} уменьшено на {amount}')
        else:
            print(f'Склад: {product} отсутствует или его значение меньше {amount}')

    def run(self, requests):
        amount_processes = len(requests)
        processes = []
        with Pool(processes=amount_processes) as pool:
            pool.map(self.process_request, requests)



if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()
    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    # Запускаем обработку запросов
    manager.run(requests)
    # Выводим обновленные данные о складских запасах
    print(manager.data)

from multiprocessing import Process, Pipe


class WarehouseManager:

    def __init__(self):
        self.data = {}

    def process_request(self, request, conn):
        product, process, value = request
        data = conn.recv()
        if process == "receipt":
            data[product] = data.get(product, 0) + value
            print(f'Склад: {product} увеличено на {value}')
        elif process == "shipment" and data.get(product, False) and data[product] >= value:
            data[product] -= value
            print(f'Склад: {product} уменьшено на {value}')
        else:
            print(f'Склад: {product} отсутствует или его значение меньше {value}')
        conn.send(data)
        conn.close()

    def run(self, requests):
        procs, pipes = [], []
        for request in requests:
            parent_conn, child_conn = Pipe()
            procs.append(Process(target=self.process_request, args=(request, child_conn)))
            pipes.append(parent_conn)
        [proc.start() for proc in procs]
        for conn in pipes:
            conn.send(self.data)
            self.data = conn.recv()
            conn.close()
        [proc.join() for proc in procs]


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

if __name__ == '__main__':
    # Запускаем обработку запросов
    manager.run(requests)
    # Выводим обновленные данные о складских запасах
    print(manager.data)

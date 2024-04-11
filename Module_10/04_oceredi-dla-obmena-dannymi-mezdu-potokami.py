import queue
import threading
import time


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:

    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue(20)

    def customer_arrival(self, number_of_customers=20):
        for i in range(1, number_of_customers + 1):
            print(f'Посетитель номер {i} прибыл')
            self.serve_customer(i)
            time.sleep(1)

    def serve_customer(self, customer):
        if all(table.is_busy for table in self.tables):
            self.queue.put(customer)
            print(f'Посетитель номер {customer} ожидает свободный стол')
        while True:
            if any(table.is_busy for table in self.tables):
                Customer(customer, self.tables)


class Customer(threading.Thread):

    def __init__(self, customer, tables):
        super().__init__()
        self.customer = customer
        self.tables = tables
        self.start()

    def run(self):
        for table in self.tables:
            if not table.is_busy:
                print(f'Посетитель номер {self.customer} сел за стол {table.number}')
                table.is_busy = True
                time.sleep(5)
                print(f'Посетитель номер {self.customer} покушал и ушел')
                table.is_busy = False
                return




# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

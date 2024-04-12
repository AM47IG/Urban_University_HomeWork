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
        self.queue = queue.Queue()

    def customer_arrival(self, number_of_customers=20):
        i = 0
        while True:
            if any((not table.is_busy) for table in self.tables) and not self.queue.empty():
                self.serve_customer(self.queue.get())
            if i < number_of_customers:
                i += 1
                self.serve_customer(Customer(i, self.tables))
            time.sleep(1)
            if self.queue.empty() and i >= number_of_customers:
                break

    def serve_customer(self, customer):
        if any((not table.is_busy) for table in self.tables):
            customer.start()
        else:
            self.queue.put(customer)
            print(f'Посетитель номер {customer.number} ожидает свободный стол')


class Customer(threading.Thread):

    def __init__(self, number, tables):
        super().__init__()
        print(f'Посетитель номер {number} прибыл')
        self.number = number
        self.tables = tables

    def run(self):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {self.number} сел за стол {table.number}')
                time.sleep(5)
                table.is_busy = False
                print(f'Посетитель номер {self.number} покушал и ушел')
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

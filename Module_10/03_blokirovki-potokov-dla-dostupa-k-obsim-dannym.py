from threading import Thread, Lock


class BankAccount:

    def __init__(self):
        self.balance = 1000
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}', flush=True)

    def withdraw(self, amount):
        with self.lock:
            self.balance -= amount
            print(f'Withdrew {amount}, new balance is {self.balance}', flush=True)


def deposit_task(account, amount):
    for _ in range(1500):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(1000):
        account.withdraw(amount)


account = BankAccount()
deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

# 5) Создайте систему управления банковскими счетами, которая позволяет создавать, управлять и выполнять операции
# с банковскими счетами различных клиентов.
# 1.	Реализуйте класс Client, представляющий клиента банка. Класс должен иметь атрибуты name (имя клиента)
# и id (уникальный идентификатор клиента).
# 2.	Реализуйте класс BankAccount, представляющий банковский счет. Класс должен иметь атрибуты account_number
# (номер счета), balance (баланс счета) и client (объект типа Client, которому принадлежит счет).
# Класс также должен иметь методы deposit(amount) и withdraw(amount), которые позволяют пополнить или снять деньги со счета.
# 3.	Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts, который является словарем,
# где ключами являются номера счетов, а значениями - объекты типа BankAccount. Класс также должен иметь
# методы create_account(client, initial_balance) для создания нового счета и get_account(account_number)
# для получения счета по его номеру.
# 4.	Добавьте в класс Bank методы для выполнения переводов между счетами (transfer(sender_account, receiver_account, amount)),
# а также для получения общего баланса клиента (get_total_balance(client)), который включает сумму денег на всех его счетах.
# 5.	Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег или отсутствие счета при переводе.

class Client:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class BankAccount:
    def __init__(self, account_number, balance, client):
        self.account_number = account_number
        self.balance = balance
        self.client = client

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Недостаточно средств')


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_number, initial_balance, client)
        self.accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, sender_account, receiver_account, amount):
        sender = self.get_account(sender_account)
        receiver = self.get_account(receiver_account)

        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Перевод на сумму {amount} выполнен успешно.")
            else:
                print("Недостаточно средств на счете отправителя.")
        else:
            print("Один из счетов не существует.")

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
        return total_balance



bank = Bank()

client1 = Client("Иванов", 1)
client2 = Client("Петров", 2)

account1 = bank.create_account(client1, 1000)
account2 = bank.create_account(client2, 500)

bank.transfer(account1, account2, 300)
bank.transfer(account2, account1, 700)

print("Баланс клиента Иванова:", bank.get_total_balance(client1))
print("Баланс клиента Петрова:", bank.get_total_balance(client2))
# Создать класс "Банк", который имеет атрибуты имя и список
# ﻿﻿счетов (экземпляров класса "Счет").
# Класс "Счет" имеет атрибуты номер и баланс.

class Account:
    def __init__(self, number, balance):
        self.number = number  # Атрибут "number" для хранения номера счета
        self.balance = balance  # Атрибут "balance" для хранения текущего баланса счета


class Bank:
    def __init__(self, name):
        self.name = name  # Атрибут "name" для хранения имени банка
        self.accounts = []  # Атрибут "accounts" для хранения списка счетов

    def add_account(self, account):
        self.accounts.append(account)  # Добавление счета в список счетов банка

    def remove_account(self, account):
        self.accounts.remove(account)  # Удаление счета из списка счетов банка

# Создание экземпляра класса "Account"
account1 = Account("123456789", 1000)

# Создание экземпляра класса "Bank"
my_bank = Bank("My Bank")

# Добавление счета в банк
my_bank.add_account(account1)

# Вывод информации о банке и счетах
print("Bank name:", my_bank.name)
print("Accounts in the bank:")
for account in my_bank.accounts:
    print("Account number:", account.number)
    print("Balance:", account.balance)
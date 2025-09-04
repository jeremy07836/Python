import datetime
import pytz

class Account:
    """ Simple account class with balance"""

    @staticmethod
    def _current_time():
        time_now = datetime.datetime.now()
        return pytz.utc.localize(time_now)

    def __init__(self, name, balance):
        self._transaction_list = []
        self.name = name
        if balance <= 0:
            self.__balance = 0
        else:
            self.__balance = balance
            self._transaction_list.append((Account._current_time(), self.__balance))
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))
        else:
            print(f"Invalid deposit amount: {amount}")
        self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print(f"Can not withdraw amount {amount}")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})"
                  .format(amount, tran_type, date.astimezone(), date))

    @property
    def balance(self):
        return self.__balance
        # return "$" + str(self._balance)


if __name__ == '__main__':
    jeremy = Account("Jeremy", 10)
    jeremy.show_balance()

    jeremy.deposit(1000)
    jeremy.deposit(-100)
    # jeremy.show_balance()
    jeremy.withdraw(500)
    jeremy.withdraw(5000)
    # jeremy.show_balance()
    # print(jeremy._balance)
    # print(jeremy.balance)     # See balance property
    # print(jeremy.transaction_list)
    jeremy.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()

    emptyAccount = Account("Empty", 0)
    emptyAccount.show_balance()
    emptyAccount.__balance = 10
    emptyAccount.show_balance()
    print(emptyAccount.__dict__)
    emptyAccount._Account__balance = 10
    emptyAccount.show_balance()

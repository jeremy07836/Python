import datetime
import pytz

class Account:
    """ Simple account class with balance"""

    @staticmethod
    def _current_time():
        time_now = datetime.datetime.now()
        return pytz.utc.localize(time_now)

    def __init__(self, name, _balance):
        self.name = name
        self._balance = _balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.transaction_list.append((Account._current_time(), amount))
        else:
            print(f"Invalid deposit amount: {amount}")
        self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print(f"Can not withdraw amount {amount}")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})"
                  .format(amount, tran_type, date.astimezone(), date))

    @property
    def balance(self):
        return self._balance
        # return "$" + str(self._balance)


if __name__ == '__main__':
    jeremy = Account("Jeremy", 0)
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

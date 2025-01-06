class BankAccount:
    """
    In class baraye modiriat hesab banki mishe estefade kard.
    Hame chiz ro mitavanid zakhire konid (shomare hesab, name karbar, balance, bank).
    """

    def __init__(self, account_number,password, account_holder_name, bank, balance=0):
        """
        vorodi ha va tavanaie estefade az oon.
        """
        self.account_number = account_number
        self.password = password
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.bank = bank

    def deposit(self, amount):
        """
        Vared kardan pool be hesab.
        """
        if amount > 0:
            self.balance += amount #agar az sefr bozorgtat edame dahad
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        """
        Keshidan pool az hesab.
        """
        if 0 < amount <= self.balance:#agar az sefr bozorgtat va az mojoodi kamtar bashad edame dahad
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Not enough funds or invalid withdrawal.")

    def get_balance(self):
        """
        chap mikone mojoodi ro.
        """
        return self.balance

    def display_info(self):
        """
        Etelaat hesab ro neshon mideh.
        """
        print(f"Account Number: {self.account_number}")
        print(f"Password: {self.password}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Balance: ${self.balance}")
        print(f"Bank: {self.bank}")

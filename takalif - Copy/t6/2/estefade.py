from file_asli import *
from time import sleep

p1 = BankAccount("6258_8449_1234_5678",9854, "Ali daie", "mellat", 100000)
a=int(input("enter amount of deposit: "))
p1.deposit(a)
n=int(input("enter amount of withdraw: "))
p1.withdraw(n)
sleep(2)
p1.get_balance()
p1.display_info()
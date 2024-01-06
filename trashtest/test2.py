from datetime import datetime
date = datetime(2024, 1, 6)
balance = input("Please input the balance: ")
fnum = float(balance)
sep = "_"

print(f"Your balance is: {fnum:{sep}.2f} and the date is: {date:%d/%m/%Y}")
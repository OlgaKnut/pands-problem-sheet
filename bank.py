# bank.py
# Author: Olga Knutova
# Description: Propmts user to enter two money amounts (in cents)
#              Prints sum of the two amounts with a euro sign
#              and decimal point.

amount1 = int(input("Enter first amount (in cents): "))
amount2 = int(input("Enter second amount (in cents): "))
sum = str(amount1 + amount2)
euro = sum [:-2]
cents = sum [-2:]
print (f'The sum of these is €{euro}.{cents}')


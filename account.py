# account.py
# Author: Olga Knutova
# Description: reads in 10 character account number,
#              outputs the account number with last 4 digits showing and the rest replased with Xs.


account_number = input("Please enter an 10 digit account number: ")
output_account_number = (account_number[6:])
print('XXXXXX{}'.format(output_account_number))


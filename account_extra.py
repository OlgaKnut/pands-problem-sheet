# account_extra.py.py
# Description: reads in any length account number,
#              outputs the account number with last 4 digits showing and the rest replaced with Xs.
# Author: Olga Knutova


account_number = input("Please enter an account number: ")
# as length of account nuber is not defined we need to find out it each time we run the program
length_of_account = len(account_number)
# than to find the position to start slising from
start = length_of_account-4
#output_account_number = account_number[start:] (gives fals results in case of 3 digit account)
output_account_number = account_number[-4:]
# The number of Xs we will print is equal to starting position of slising 
# we create string with value "X" and repeat it (ref.https://www.oraask.com/wiki/python-repeat-string)
str1="X"
print(f"{str1 * start}{output_account_number}")

# after running this program with account length less than 5 I noticed that instead of calculating starting point
# it is possible to use negative number.
# output_account_number = account_number[-4:]
# this way we will avoid printing only last digit of 3 digits account  number(3-4=-1)
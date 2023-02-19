# collatz.py
# Author: Olga Knutova
# Description: asks the user to input any positive integer 
#               outputs the successive values of the folowing calculation.
#               at each step calcilate the next value by taking current value and,
#               if it is even, divide it by two,
#               if it is odd, multiply it by three and add one.
#               Ends if the current value is one.


current_value = int(input("Please enter a positive integer: "))
while current_value != 1:
        if(current_value % 2) == 0:
            new_current_value = (current_value/2)
            print (int(new_current_value))
            current_value=new_current_value
        else:
            new_current_value = int(current_value*3+1)
            print (new_current_value)
            current_value=new_current_value
# squareroot.py
# Author: Olga Knutova
# Description: takes a positive floating-point number as input and outputs an approximation of its square root.



def sqrt (N,L = 0.01):  #L- is a tolerance level. Set to defolt value, 
                        #but can be changed if more accurat results needed
        root = N/2  #assumtion to start the loop, could be any number.
        while abs(root**2 - N) > L:
            root = 0.5* (root + (N/root)) 
            #https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
            #in each loop a new value given to the "root" till (root**2-N) gets close to 0 (from -0.1 to 0.1)
        return root   

N = float(input ( "Please enter a positive number: "))
ans = sqrt(N)
print (f"The square root of {N} is approx {ans:.1f}")




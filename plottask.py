# plottask.py
# Author: Olga Knutova
# Description: displays: a histogram of normal distribution of 1000 values with mean of 5 
#                           and standard deviation of 2,
#                        and a plot of the function h(x)=x3 in the range [0, 10]

import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(5, 2, 1000)

plt.hist(x, color='aqua', edgecolor='blue', label='normal distribution')

xpoints = np.array(range(0,10))
ypoints = pow(xpoints, 3)
#https://www.w3schools.com/python/ref_func_pow.asp#:~:text=Python%20pow%20%28%29%20Function%201%20Definition%20and%20Usage,Examples%20Example%20Get%20your%20own%20Python%20Server%20

plt.plot(xpoints, ypoints, ls='dashed', color='m', marker = '*', ms=10, mfc='r', label='h(x)=x3')
plt.title("PLOT TASK")
plt.grid(color = 'grey', linestyle = ':', linewidth = 0.5)
plt.legend()
#https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
plt.show()

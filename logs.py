# logs.py
#
# Outputs the value of g(x) = ln(100-x^2) + sqrt(84 - 5x - x^2) at the input x-value.

import math

#Defining Function
def g(x):
    return math.log(100 - x**2) + math.sqrt(84 - 5*x - x**2)

#Converting Inputs to Floats
x = input("Input the value for x: ")
x = float(x)

#If then statments
if x <= -10 or x > 7:
    print('Invalid number, Program does not work please input a valid number')
    exit()

#Printing Answer
print("g(" + str(x) + ") = " + str(g(x)))

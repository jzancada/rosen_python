# example
# min y=x(0)**2+x(1)**2
# with the following linear restrictions:
# x(0) > 0
# x(0) < 10
# x(1) > 0
# x(1) < 10
# a00*x(0)+a01*x(1) > b0
# a10*x(0)+a11*x(1) > b1

import numpy as np 

# function
def f(x):
    y=x[0]**2+x[1]**2
    return y

# gradient
def g(x):
    y = 2*x[0]+2*x[1]
    return y

x=(10,2)
print('f = x', x, f(x))

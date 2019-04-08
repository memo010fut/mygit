x = [1.0,1.6,3.4,4.0,5.2]
y = [1.2,2.0,2.4,3.5,3.5]

def suma(a):
    sum = 0
    for i in range(len(a)):
        sum = a[i] + sum
    return sum

print (suma(x))
print (suma(y))

import pandas as pd

x1 = pd.array(x)
print (x1)
y1 = pd.array(y)
print (y1)

xy = x1 * y1
print (xy)


x2 = x1 * x1
print (x2)

n = len(x)
print(n)


def lin_reg(m,n):
    xf = pd.array(m)
    yf = pd.array(n)
    n = len(m)

    a = ((n*suma(xf*yf))-(suma(xf)*suma(yf)))/((n*(suma(xf*xf)))-(suma(xf)*suma(xf)))
    #a = (suma(xf * yf))
    b = ((suma(yf)*suma(xf*xf))-(suma(xf*yf)*suma(xf)))/((n*(suma(xf*xf)))-(suma(xf)*suma(xf)))

    return a, b

print(lin_reg(x, y))

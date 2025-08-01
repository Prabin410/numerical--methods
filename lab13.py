##to evaluate by trapezodial rule
import numpy as np
import matplotlib.pyplot as plt

a=float(input('Enter lower limit: '))
b=float(input('Enter upper limit: '))
n=int(input('Enter number of partions: '))
h=float((b-a)/n)
fu=input('Enter the integrand function f(x): using x as variable: ')
def f(x,fu):
    return eval(fu)
def y(x):
    return f(x,fu)
x=np.linspace(a, b, n+1)
integral=0
sum=0
for i in range(1, n):
    sum+=y(x[i])
integral=(h/2)*(y(x[0]) + 2*sum + y(x[n]))
print(f'The value of integral by trapezodial rule is: {integral}')

##to evaluate by trapezodial rule
import numpy as np
import matplotlib.pyplot as plt

a=float(input('Enter lower limit: '))
b=float(input('Enter upper limit: '))
n=int(input('Enter number of partions: '))
assert n%2==0,"n should be even for simpson's rule"
h=float((b-a)/n)
fu=input('Enter the integrand function f(x): using x as variable: ')
def f(x,fu):
    return eval(fu)
def y(x):
    return f(x,fu)
x=np.linspace(a, b, n+1)
integral=0
sum_odd=0
sum_even=0
for i in range(1, n):
    if i % 2 == 0:
        sum_even += y(x[i])
    else:
        sum_odd += y(x[i])
integral=(h/3)*(y(x[0]) + 4*sum_odd + 2*sum_even + y(x[n]))

print(f'The value of integral by simpson\'s rule is: {integral}')
xval=np.linspace(a-10, b+10, 1000)
yval=[y(value) for value in xval]  
plt.plot(xval,[y(x) for x in xval], label='Integrand function')
plt.plot(x,[y(x) for x in x], label='partition points')
plt.axhline(0,0)
plt.axvline(0,0)

ypoints=[y(x) for x in x]
for i in range(n):
    x_list=[x[i],x[i],x[i+1],x[i+1]]
    y_list=[0,ypoints[i],ypoints[i+1],0]
    plt.fill(x_list, y_list, color='blue',edgecolor='black', alpha=0.5, label='Area under curve')
plt.show()
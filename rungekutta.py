import numpy as np
import pandas as pd
import matplotlib as plt
ode=input("Enter dy/dx in form of x and y using python syntax")
def F(x,y,ode):
    return eval (ode)
def f(x,y):
    return F(x,y,ode)
x=float(input("enter initial value of x"))
y=float(input("enter initial value of y"))
h=float(input("enter the step size"))
n=int(input("enter no of times")) 
T=[]
x_val=[]
y_val=[]
for i in range(n):
    k1=h*f(x,y)
    k2=h*f(x+h/2,y+k1/2) 
    k3=h*f(x+h/2,y+k2/2)
    k4=h*f(x+h,y+k3)
    y=y+(1/6)*(k1+2*k2+2*k3+k4)
    x=x+h
   
    T.append([x,y])
   
    x_val.append(x)
    y_val.append(y)
T=pd.DataFrame(T,columns=['x','y'])
print("Solutions are")
print(T)
plt.plot(x_val,y_val,label='curve',color='red')
plt.scatter(x_val,y_val,label='points',color='blue')

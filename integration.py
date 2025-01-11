

import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_y(x):
    y=(-1)*(6.73*x+4.3025e-7)/((2.316e-11)*x)
    return y



def trapizoidalRule(a,b,n):
    sum=0;
    h=(b-a)/n
    sum=sum+calculate_y(a)+calculate_y(b)

    for i in range(1,n):
        sum=sum+2*calculate_y(a+i*h)

    sum=sum*(b-a)/(2*n)
    return sum;

def errorTableForTrapizoidal(a,b,n):
    print("\n")
    print("from trapezoidal rule:...........\n")
    cur=trapizoidalRule(a,b,1)

    print("n","\t\t\t","value of integral","\t\t\t","absolute relative error",end="\n")

    print(1,"\t\t\t",round(cur,5),end="\n")
    prev=cur
    for i in range(2,n+1):
        cur=trapizoidalRule(a,b,i)
        error=abs(prev-cur)*100/cur
        print(i,"\t\t\t",round(cur,5),"\t\t\t",error,end="\n")
        prev=cur



def simpsonsRule(a, b, n):
    sum=0;
    h=(b-a)/n
    sum=sum+calculate_y(a)+calculate_y(b)

    for i in range(1,n,2):
        sum=sum+4*calculate_y(a+i*h)
    for i in range(2,n-1,2):
        sum=sum+2*calculate_y(a+i*h)

    sum=sum*(b-a)/(3*n)
    return sum;

def errorTableForSimpsons(a,b,n):
    print("\n")
    print("from simpsons rule:...........\n")
    cur=simpsonsRule(a,b,2)

    print("n","\t\t\t","value of integral","\t\t\t","absolute relative error",end="\n")

    print(2,"\t\t\t",round(cur,5),end="\n")
    prev=cur
    for i in range(4,n+1,2):
        cur=simpsonsRule(a,b,i)
        error=abs(prev-cur)*100/cur
        print(i,"\t\t\t",round(cur,5),"\t\t\t",error,end="\n")
        prev=cur



def drawGraph():
    x=[1.22e-4,1.20e-4,1.0e-4,0.8e-4,0.6e-4,0.4e-4,0.2e-4]
    y=[]
    y.append(0)
    for i in range(1,7):
        y.append(simpsonsRule(x[0],x[i],10))

    npx=np.array(x)
    npy=np.array(y)
    plt.plot(npx,npy,marker='o')
    plt.xlabel("concentraiton of oxygen(moles/cc)")
    plt.ylabel("time(seconds)")
    plt.grid()
    plt.show()






n=int(input())



print("value from trapezoidal rule................\n")

print(trapizoidalRule(1.22e-4,0.5*1.22e-4,n))

errorTableForTrapizoidal(1.22e-4,0.5*1.22e-4,5)




print("value from simpson's rule...................\n")

print(simpsonsRule(1.22e-4,0.5*1.22e-4,2*n))

errorTableForSimpsons(1.22e-4,0.5*1.22e-4,10)


drawGraph()
















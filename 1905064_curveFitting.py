
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=5,suppress=True)
from math import e, log








def calculateSumX(x,n,power):
    sum=0
    for i in range(0,n):
        sum+=pow(x[i],power)

    return sum

def calculateSumXY(x,y,n,powerX,powerY):
    sum=0
    for i in range(0,n):
        sum=sum+pow(x[i],powerX)*pow(y[i],powerY)

    return sum

def linearModel(x,y,n):
    a=[]

    a0=calculateSumX(x,n,2)*calculateSumX(y,n,1)-calculateSumX(x,n,1)*calculateSumXY(x,y,n,1,1)
    a0=a0/(n*calculateSumX(x,n,2)-calculateSumX(x,n,1)**2)
    a.append(a0)

    a1=n*calculateSumXY(x,y,n,1,1)-calculateSumX(x,n,1)*calculateSumX(y,n,1)
    a1=a1/(n*calculateSumX(x,n,2)-calculateSumX(x,n,1)**2)
    a.append(a1)

    return a





def drawGraphToAssumeModel(x,y):
    npx = np.array(x)
    npy = np.array(y)

    # plot the function
    plt.scatter(npx, npy, color='g',marker='o')
    # plt.plot(npx, npy, color='g',marker='o')
    plt.grid()
    plt.xlabel('hours since drug was administered')
    plt.ylabel('amount of drug in body')
    # show the plot
    plt.show()

def calculateY(x,a):
    y=a[0]*e**(a[1]*x)
    return y

def testTheEquation(x,y,a):
    npx = np.array(x)
    npy = np.array(y)

    # plot the function
    plt.scatter(npx, npy, color='r', marker='o')
    # plt.plot(npx, npy, color='g',marker='o')

    x1 = np.arange(0, 30, 0.1)
    y1 = calculateY(x1,a)

    # plot the function
    plt.plot(x1, y1, 'g')
    plt.grid()
    plt.xlabel('hours since drug was administered')
    plt.ylabel('amount of drug in body')
    # show the plot
    plt.show()








def changeY(y,n):
    z=[]
    for i in range(n):
        z.append(log(y[i],e))
    return z;





n=7
x=[0,5,10,15,20,25,30]
y=[1000,550,316,180,85,56,31]




drawGraphToAssumeModel(x,y)  # to assume the model we have plotted the points..........

#we can write y=a*e^(bx) as lny=lna+bx now our function is turned into a linear.
# here we have taken z=lny, a0=lna and a1=b
z=changeY(y,7)


a=linearModel(x,z,n)  # returns an array with two constants (lna and b)..........
a[0] = e**a[0]  # converting  lna into a..............



# for i in range(2):
#     print(a[i])

testTheEquation(x,y,a)
print("the equation is y=(",a[0],")e^(",a[1],"x)")


print("after 40 hours the amount:   ")

print(calculateY(40,a))






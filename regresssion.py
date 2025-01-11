import numpy as np
import matplotlib.pyplot as plt
import math as m




#gaussian elimination for polynomial model........................................

def pivotRow(A,B,rowToStart,colNo,varNo):
    mx=0
    rowToSwap=rowToStart
    for i in range(rowToStart,varNo):
        if(mx<A[i][colNo]):
            mx=A[i][colNo]
            rowToSwap=i

    A[[rowToStart,rowToSwap]]=A[[rowToSwap,rowToStart]]
    B[[rowToStart, rowToSwap]] = B[[rowToSwap, rowToStart]]

def makingColumnZero(A,B,colNo,pivot,varNo):
    if pivot:
        pivotRow(A,B,colNo,colNo,varNo)


    for i in range(colNo+1,varNo):
        mul = A[i][colNo] / A[colNo][colNo]
        for j in range(colNo,varNo):
            A[i][j]=A[i][j]-(A[colNo][j]*mul)

        B[i]=B[i]-B[colNo]*mul

def forwardElimination(A,B,pivot,showall,varNo):

    for i in range(0,varNo-1):
        makingColumnZero(A,B,i,pivot,varNo)

        if (showall == True):
            print("step ", i+1, ":  ")
            print(A)
            print("\n")
            print(B)
            print("\n\n")

def backwardSubstitution(A,B,pivot,varNo,results):

    for i in range(varNo):
        pre=B[varNo-1-i]
        for j in range(i):
            pre=pre-A[varNo-1-i][varNo-1-j]*results[j]
        pre=pre/A[varNo-1-i][varNo-1-i]
        results.append(pre)


def GaussianElimination(A,B,varNo,pivot,showall):
    results = []
    forwardElimination(A, B, pivot,showall,varNo)
    backwardSubstitution(A, B, pivot,varNo,results)
    results.reverse()
    return results




#bisection method for exponential model......................................

def bisection(l,u,e,itr,old_val,x,y,n):
    m=(l+u)/2
    mid=calculateYforB(x,y,n,m)

    if old_val!=1e18:
        cur_e=(abs(m-old_val)/m)*100

        if mid==0:
            return m
        if cur_e<e:
            return m

    if itr==1:
        return m


    rValue=calculateYforB(x,y,n,u)
    if rValue*mid<0:
        return bisection(m,u,e,itr-1,m,x,y,n)
    else:
        return bisection(l,m,e,itr-1,m,x,y,n)





# calculation of different sums................................................

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

def calculateSumXYebx(x,y,n,b,powerX,powerY):
    sum=0
    for i in range(n):
        e=m.exp(1)
        sum+=pow(x[i],powerX)*pow(y[i],powerY)*pow(e,(b*x[i]))

    return sum






# finding initial values of b (exponential model) and solving b through bisection................................

def calculateYforB(x,y,n,b):
    p=calculateSumXYebx(x,y,n,b,1,1)-(calculateSumXYebx(x,y,n,b,0,1)*calculateSumXYebx(x,y,n,2*b,1,0))/calculateSumXYebx(x,y,n,2*b,0,0)
    return p

def drawGraphToAssumeB(x,y,n):
    npx = np.arange(20, 30, 0.0001)
    npy = calculateYforB(x, y, n, npx)


    # plot the function
    plt.plot(npx, npy, 'g')
    plt.grid()
    plt.xlabel('b->')
    plt.ylabel('f(b)')
    # show the plot
    plt.show()









def linearModel(x,y,n):
    a=[]

    a0=calculateSumX(x,n,2)*calculateSumX(y,n,1)-calculateSumX(x,n,1)*calculateSumXY(x,y,n,1,1)
    a0=a0/(n*calculateSumX(x,n,2)-calculateSumX(x,n,1)**2)
    a.append(a0)

    a1=n*calculateSumXY(x,y,n,1,1)-calculateSumX(x,n,1)*calculateSumX(y,n,1)
    a1=a1/(n*calculateSumX(x,n,2)-calculateSumX(x,n,1)**2)
    a.append(a1)

    return a

def polynomialModel(x,y,n,order):
    arrA=[]
    for i in range(order+1):
        for j in range(order+1):
            arrA.append(calculateSumX(x,n,i+j))

    a=np.reshape(arrA,(order+1,order+1))


    arrB=[]
    for i in range(order+1):
        arrB.append(calculateSumXY(x,y,n,i,1))

    b=np.reshape(arrB,(order+1,1))

    results=GaussianElimination(a,b,order+1,True,False)
    return results

def exponentialModel(x,y,n):
    a=[]
    a1=bisection(20,26,0.0005,30,1e18,x,y,n)
    a0=calculateSumXYebx(x,y,n,a1,0,1)/calculateSumXYebx(x,y,n,2*a1,0,0)
    a.append(a0)
    a.append(a1)

    return a







def drawGraphToAssumeModel(x,y):
    npx = np.array(x)
    npy = np.array(y)

    # plot the function
    plt.scatter(npx, npy, color='g',marker='o')
    # plt.plot(npx, npy, color='g',marker='o')
    plt.grid()
    plt.xlabel('x->')
    plt.ylabel('y')
    # show the plot
    plt.show()

def drawTheEquation(a):
    x = np.arange(-340, 80, 0.0001)
    y = calculateY(x,a)

    # plot the function
    plt.plot(x, y, 'g')
    plt.grid()
    plt.xlabel('X->')
    plt.ylabel('Y')
    # show the plot
    plt.show()







def calculateY(x,a):
    y=a[0]+a[1]*x+a[2]*x**2+a[3]*x**3
    return y

def testTheEquation(x,y,a):
    npx = np.array(x)
    npy = np.array(y)

    # plot the function
    plt.scatter(npx, npy, color='g', marker='o')
    # plt.plot(npx, npy, color='g',marker='o')

    x1 = np.arange(1900, 2000, 0.1)
    y1 = calculateY(x1,a)

    # plot the function
    plt.plot(x1, y1, 'g')
    plt.grid()
    plt.xlabel('X->')
    plt.ylabel('Y')
    # show the plot
    plt.show()


n=11
x=[1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]
y=[10.3,13.5,13.9,14.2,11.6,10.3,9.7,9.6,14.1,19.8,31.1]

# x=[80,40,-40,-120,-200,-280,-340]
# y=[0.00000647,0.00000624,0.00000572,0.00000509,0.00000430,0.00000333,0.00000245]

# n=int(input("enter the number of points\n"))
#
# for i in range(n):
#     x.append(float(input()))
# for i in range(n):
#     y.append(float(input()))

# a=linearModel(x,y,n)
# b=polynomialModel(x,y,n,2)


# drawGraphToAssumeB(x,y,n)
#
# drawGraphToAssumeModel(x,y)



a=polynomialModel(x,y,n,3)
for i in range(4):
    print(a[i])
# drawTheEquation(a)
testTheEquation(x,y,a)
#print(b)
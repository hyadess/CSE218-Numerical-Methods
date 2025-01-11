
import numpy as np
import matplotlib.pyplot as plt
from array import *


np.set_printoptions(precision=4,suppress=True)



varNo=int(input())

inputA=[]
for i in range(varNo):
    l=list(map(float,input().split()))
    inputA.extend(l)

# print(inputA)
# for i in range(varNo*varNo):
#     inputA.append(float(input()))

inputB=[]
for i in range(varNo):
    inputB.append(float(input()))


a=np.reshape(inputA,(varNo,varNo))
b=np.reshape(inputB,(varNo,1))








def pivotRow(A,B,rowToStart,colNo):
    mx=0
    rowToSwap=rowToStart
    for i in range(rowToStart,varNo):
        if(mx<A[i][colNo]):
            mx=A[i][colNo]
            rowToSwap=i

    A[[rowToStart,rowToSwap]]=A[[rowToSwap,rowToStart]]
    B[[rowToStart, rowToSwap]] = B[[rowToSwap, rowToStart]]

def makingColumnZero(A,B,colNo,pivot):
    if(pivot):
        pivotRow(A,B,colNo,colNo)


    for i in range(colNo+1,varNo):
        mul = A[i][colNo] / A[colNo][colNo]
        for j in range(colNo,varNo):
            A[i][j]=A[i][j]-(A[colNo][j]*mul)

        B[i]=B[i]-B[colNo]*mul
        print("step -----------", ":  ")
        print(A)
        print("\n")
        print(B)
        print("\n\n")

def forwardElimination(A,B,pivot,showall):

    for i in range(0,varNo-1):
        makingColumnZero(A,B,i,pivot)

        if (showall == True):
            print("step ", i+1, ":  ")
            print(A)
            print("\n")
            print(B)
            print("\n\n")



results=[]
def backwardSubstitution(A,B,pivot):

    for i in range(varNo):
        pre=B[varNo-1-i]
        for j in range(i):
            pre-=A[varNo-1-i][varNo-1-j]*results[j]
        pre=pre/A[varNo-1-i][varNo-1-i]
        results.append(pre)




def GaussianElimination(A,B,pivot,showall):
    forwardElimination(A, B, pivot,showall)
    backwardSubstitution(A, B, pivot)











GaussianElimination(a,b,True,True)
results.reverse()

print("answer matrix:  ")

# print(a)
# print(b)
print(np.reshape(results,(varNo,1)))


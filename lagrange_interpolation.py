
import numpy as np
import matplotlib.pyplot as plt
import math



def read_file(a,b):
    file=open("stock.txt")
    i=0
    for line in file:
        if(i!=0):
            data=line.split("\t")
            a.append(int(data[0]))
            b.append(float(data[1]))
        i=i+1

    file.close()


def sort_points_around_theGivenPoint(used_x,used_y,x,y,totalPoints,givenPoint):
    difference=[]
    for i in range(totalPoints):
        difference.append(abs(x[i]-givenPoint))
    difference=sorted(difference)
    tempx=x.copy()
    tempy=y.copy()

    for i in range(totalPoints):
        for j in range(totalPoints):
            if abs(tempx[j] - givenPoint)==difference[i]:
                used_x[i]=tempx[j]
                used_y[i]=tempy[j]
                break

def finding_L_for_lagrange(x,l,order,givenPoint):
    for i in range(order+1):
        rep=1;
        for j in range(order+1):
            if(j!=i):
                rep=rep*(givenPoint-x[j])/(x[i]-x[j])
        l[i]=rep
    return l

def findingValueWithLagrange(l,x,y,order,givenPoint):
    l=finding_L_for_lagrange(x,l,order,givenPoint)
    ans=0;
    for i in range(order+1):
        ans+=l[i]*y[i]

    return ans;

def graphPlotting(a,b,day,cubic_ans):
    tempa=a.copy()
    tempb=b.copy()

    # a.append(day)
    # b.append(cubic_ans)
    x=np.array(tempa)
    y=np.array(tempb)

    # axhline(y=0, color='k')
    # axvline(x=0, color='k')

    plt.plot(x,y)
    plt.plot(day,cubic_ans,marker='o')
    plt.show()




#start of main............................


x=[]
y=[]

read_file(x,y)

l=[]
used_x=[]
used_y=[]
for i in range(len(x)):
    l.append(0)
    used_x.append(0)
    used_y.append(0)


day=int(input("enter the day\n"))


sort_points_around_theGivenPoint(used_x,used_y,x,y,len(x),day)


# print(x)

cubic_ans=findingValueWithLagrange(l,used_x,used_y,3,day)
quadratic_ans=findingValueWithLagrange(l,used_x,used_y,2,day)

error=math.fabs((cubic_ans-quadratic_ans)/cubic_ans)*100

graphPlotting(x,y,day,cubic_ans)



print(cubic_ans)
print(error)

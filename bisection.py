import math

import numpy as np
import matplotlib.pyplot as plt

from array import *


def calculate_y(x):
    return x**2-0.5-math.sin(x)



# def draw_graph():
#     x=np.arange(-0.1,0.2,0.0001)
#     y=calculate_y(x)
#
#
#     # plot the function
#     plt.plot(x,y, 'g')
#     plt.grid()
#     plt.xlabel('X->')
#     plt.ylabel('Y')
#     # show the plot
#     plt.show()
#
# draw_graph()

# from the graph we can say that our result lies between 0.05 to 0.10....





def bisection(l,u,e,itr,old_val):
    m=(l+u)/2
    y=calculate_y(m)

    if old_val!=1:
        cur_e=(abs(m-old_val)/m)*100

        if y==0:
            return m
        if cur_e<e:
            return m

    if itr==1:
        return m


    if calculate_y(l)*calculate_y(m)>0:
        return bisection(m,u,e,itr-1,m)
    else:
        return bisection(l,m,e,itr-1,m)

def bisection_table(l,u,e,itr,old_val):
    m=(l+u)/2
    y=calculate_y(m)

    cur_e=100
    if old_val!=1:
        cur_e=(abs(m-old_val)/m)*100

    print(5-itr,end='                       ')
    print(l, end='                       ')
    print(u, end='                       ')
    print(m, end='                       ')
    print(cur_e)

    if itr==0:
        return

    if calculate_y(l)*calculate_y(m)>0:
        bisection_table(m,u,e,itr-1,m)
    else:
        bisection_table(l,m,e,itr-1,m)






e=input("enter your preferred absolute approx. error\n")
itr=input("enter your preferred iteration number\n")

print("the value of x is:")
print(bisection(0.05,0.10,float(e),int(itr),1))





print('\n\n')
print('showing the table of relative approx. errors')
print('\n\n')




print('iteratons',end='             ')
print('lValue',end='             ')
print('rValue',end='             ')
print('mid',end='             ')
print('relative approx. error')
bisection_table(-1,0,float(e),5,1)























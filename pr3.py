# 6a + 9b + 20c =n
from math import *
n=int(input("Enter the amount of Nuggets You wanna buy : "))

sa=0
sb=0
sc=0
a=0
def swap1():
    global p1
    global p2
    temp=p1
    p1=p2
    p2=temp
def swap2():
    global p2
    global p3
    temp=p2
    p2=p3
    p3=temp
while((6*a)<=n):
    p1=0
    p2=0
    p3=0
    count1=0
    mid=0
    if a!=0:
        mid = int(floor(a/2))+1
    else:
        mid=0
    for i1 in range(mid):
        p1 = int(a) - count1
        count2 = 0
        a2 = int(a) - p1
        mid2 = 0
        if a2 != 0:
            mid2 = int(floor(float(a2) / 2)) + 1
        else:
            mid2 = 0
        for i2 in range(mid2):
            p2 = a2 - count2
            count3 = 0
            a3 = a2 - p2
            p3 = 0
            mid3 = 0
            if a3 != 0:
                mid3 = int(floor(float(a3) / 2)) + 1
            else:
                mid3 = 0
            for i3 in range(mid3):
                p3 = a3 - count3
                for loop1 in range(3):


                        sa=p1
                        sb=p2
                        sc=p3
                    swap2()
                    if ((6*p1+9*p2+20*p3)==n):
                        sa=p1
                        sb=p2
                        sc=p3
                    swap1()

                count3 += 1
            if (a3 == 0):
                for loop1 in range(3):
                    if ((6*p1+9*p2+20*p3)==n):
                        sa=p1
                        sb=p2
                        sc=p3
                    swap2()
                    if ((6*p1+9*p2+20*p3)==n):
                        sa=p1
                        sb=p2
                        sc=p3
                    swap1()
            count2 += 1
        if (a2 == 0):
            for loop1 in range(3):
                if ((6 * p1 + 9 * p2 + 20 * p3) == n):
                    sa = p1
                    sb = p2
                    sc = p3
                swap2()
                if ((6 * p1 + 9 * p2 + 20 * p3) == n):
                    sa = p1
                    sb = p2
                    sc = p3
                swap1()
        count1 += 1
    a+=1
if(n==0 ):
    print ("Buy  0* pack of 6 , 0* pack of 9 , 0* pack of 20")
if sa==0 and sb==0 and sc==0 :
    print("No you can't Buy Nuggets in any combination")
else :
    print("Yes You can Buy %d Nuggets"% (n))
    print( "Buy %d * pack of 6 , %d * pack of 9 , %d * pack of 20 "%(sa,sb,sc))
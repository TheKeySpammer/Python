from math import *
print("Showing 3 Partitions of a number in all possible ways")
a=float(input("Enter your number : "))
count1=0
p1=0
p2=0
p3=0
mid=0
if a!=0:
   mid= int(floor(a/2))+1
else:
    mid =0
for i1 in range(mid):
    p1=int(a)-count1
    count2=0
    a2=int(a)-p1
    mid2=0
    if a2!=0:
       mid2=int(floor(float(a2)/2))+1
    else:
        mid2=0
    for i2 in range(mid2):
        p2=a2-count2
        count3=0
        a3=a2-p2
        p3=0
        mid3=0
        if a3!=0:
           mid3=int(floor(float(a3)/2))+1
        else:
            mid3=0
        for i3 in range(mid3):
            p3=a3-count3
            print("%d , %d , %d "% (p1, p2, p3))
            count3+=1
        if(a3==0):
            print("%d , %d , %d " % (p1, p2, p3))
        count2+=1
    if(a2==0):
        print("%d , %d , %d " % (p1, p2, p3))
    count1+=1




from math import *
limit = int(input("Enter the value of n : "))
co=1
x=1.0
sum = log(2)
while x<=limit :
    x+=2.0
    x1=int(x)
    count=0
    for i in range(x1):
        if i>1 and i<x1 :
            if x1%i==0:
                count+=1
                break
    if count == 0:
        sum = sum + log(x)
print ("The Value of n is : " , limit)
print("Sum of log of prime less than or equal to n is : " , sum )
print("Ratio of the two is : " , (sum/limit))
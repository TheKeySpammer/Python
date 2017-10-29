x=1
co=1
keep =0
while x>0 :
    x+=2
    count=0
    for i in range(x):
        if i>1 and i<x :
            if x%i==0:
                count+=1
                break
    if count == 0:
        co+=1
    if co==10000:
        keep=x
        break

print( "The 10000th prime number is : ", keep)




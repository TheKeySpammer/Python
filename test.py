
a=1
b=2
c=3
def swap1():
    global a
    global b
    temp=a
    a=b
    b=temp
def swap2():
    global b
    global c
    temp=b
    b=c
    c=temp
for i in range(3):
    print("%d , %d , %d "%(a,b,c))
    swap2()
    print("%d , %d , %d " % (a, b, c))
    swap1()

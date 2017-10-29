print("THis is the list of all twin prime till 1,000,000")
def prime_check(num):
    count=0
    for x in range(num):
        if x>1 and x<num:
            if num%x==0:
                count = count+1
                break
    if count >0:
        return False
    else:
        return True
for y in range (1000000):
    if prime_check(y) and prime_check(y+2):
        print(str(y)+" , "+str((y+2)))

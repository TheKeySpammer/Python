print("Plz Enter your number TO check if its prime")
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
number= int(input("Enter:"))
b=prime_check(number)
if b:
    print("yes its prime")
else:
    print("no its not prime")




#good luck have fun
key = input("Enter your key : \n")
target = input("Enter the target : \n")
count2=0
scount=0
for i in range(len(target)-len(key)+1):
    count1=0
    if(key[count1]==target[count2]):
        count1=count1+1
        if(key[count1:len(key)]==target[count2+1:(count2+len(key))]):
            scount=scount+1
            #count2=count2+len(key)
    count2=count2+1
print("Key appeared %d times in target. "%(scount))

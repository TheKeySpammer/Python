import sys
import random
print ("if u want to exit type exit and press enter")
print( "If you know the word type it and press enter")
print("WELCOME TO WORD GAME ")
myWord = ["hello","animal","horse","king",'knight',"claustrophobia","rabbit",'python','computer','alligator','university','joker','bat','car','code']
ra=random.randint(0,14)
x=myWord[ra];
dash="--------------------"
dash=dash[0:len(x)]
word=list(dash)
for i in range(len(x)):
    print(word[i], end='')
print()
def current(a):
    for i in range(word):
        if (i!=a):
            print(word[i], end='')
        else :
            print(x[i],end='')
    print()
print("Length Of the word is :",len(x))
while(x!=word):
    cr = 0
    cw = 0
    letter=input("Guess a letter\n")
    if(letter=="exit"):
        sys.exit()
    if(letter==x):
        print("Great you did it")
        sys.exit()
    for i in range(len(x)):
        if(x[i]==letter):
          word[i]=letter
          cr+=1

    if(cr>0):
        for i in range(len(x)):
            print(word[i],end='')
        print()
        print("Great try again!")
    if(cr==0):
        print("Sorry Try again")
print("Thanks for playing")








import random

L=["rock","paper","scissor"]
userwin=0
computerwin=0
e=input('enter your name       -     ').lower()
print("welcome!!", e)
print("are you ready to play rock paper and scissors/press q to quit")

while True:
    c=input("choose rock,paper,scissor and when you feel like quitting just press q  ").lower()
    if c=="q":
        break
    elif c not in L:
        print("choose something valid")
        continue
    a=random.randint(0,2)
    computer=L[a]
    print("coputer chose",computer)
    
    if c==computer:
        print("its a draw")
    
    elif c=="paper" and computer=="rock":
        print(e,"wins!!!!")
        userwin=userwin+1
    elif c=="rock" and computer=="scissors":
        print(e,"wins!!!!")
        userwin=userwin+1
    elif c=="scissors" and computer=="paper":
        print(e,"wins!!!!")
        userwin=userwin+1
    else:
        print("sorry, computer wins..better luck next time")
        computerwin=computerwin+1
        
    
    
print(" ok ,so we are exiting")
if userwin>computerwin:

    print("congratulations!!!!",e, "wins by",userwin, "score")
    print("tata byee byee, see you next time")

elif computerwin>userwin:
    print("computer wins by",computerwin,"score")
    print("tata byee byee, see you next time")
    

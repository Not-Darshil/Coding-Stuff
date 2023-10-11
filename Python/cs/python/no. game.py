sa=sb=a=b=0
from random import *
for w in range (52):
    print()
    print("Enter space if wanna continue")
    x=input("ENTER")
    if x==" ":
        print()
        a=randint(1,6)
        b=randint(1,6)
        print("A - ",a)
        print("B - ",b)
        sa=sa+a
        sb=sb+b
        print("score of a is ",sa)
        print("score of b is ",sb)
        if sa==sb:
            if sa>50:
                print("It's a Tie")
                break
        if sa>sb:
            if sa>=50:
                print("A wins the match")
                break
        if sb>sa:
            if sb>=50:
                print("B wins the match")
                break
        if sa>=50:
            print("A wins the match")
            break
        if sb>=50:
            print("B wins the match")
            break
        
        
        

for w in range(3,101):
    p=0
    for a in range(2,w):
        if w%a==0:
            p=1
            break
    if p==1:
        z=0
    else:
        print(w,"is a prime")
    

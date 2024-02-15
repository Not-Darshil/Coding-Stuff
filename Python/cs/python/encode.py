def fn(st):
    k=""
    for w in st:
        if w.isalpha():
            if w=="z":
                k=k+"a"
            elif w=="Z":
                k=k+"A"
            else:
                k=k+(chr(ord(w)+1))
        else:
            k=k+w
    print(k)
fn("Zcomputerz12*")


def srh(x):
    en=""
    for w in x:
        if w.isalpha():
            if w=="A":
                en=en+"Z"
            elif w=="a":
                en=en+"z"
            else:
                en=en+(chr(ord(w)-1))
        else:
            en=en+w
    print(en)
srh("Adpnqvufsa12$%")
            
            

def w():
    import csv
    f=open("csvfile.csv","w+")
    wr=csv.writer(f)
    lst=["author","tile","price"]
    wr.writerow(lst)
    print("Enter details and blank details for exit")
    while True:
        lst=[]
        author=input("Enter Author Name:")
        title=input("Enter Title")
        price=int(input("Enter Price:"))
        if author=="" and price==0 and title=="":
            break
        else:
            lst.append(author)
            lst.append(title)
            lst.append(price)
            wr.writerow(lst)
#w()
        
def r():
    f=open("csvfile.csv","r")
    r=csv.reader(f)
    hd=next(r)
    print("Header",hd)
    print()
    for w in r:
        print(w)
    

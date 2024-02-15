def fn (a):
    p=0
    q=1
    b=int(len(a))
    for w in range(int(b/2)):
        a[p],a[q]=a[q],a[p]
        p=p+2
        q=q+2
    print(a)
fn([0,1,2,3,4,5])


        
    

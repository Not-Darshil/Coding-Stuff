##n=1
##l=8
##m=int(l/2)
##for w in range(l):
##    print(" "*m,"*"*n,"*"*n," "*m,sep="")
##    n=n+1
##    m=m-1
##    if m<0:
##        break
##    **    
##   ****   
##  ******  
## ******** 
##**********
##
##
##l=5
##m=1
##for w in range(5):
##    print(" "*l,"*"*m," "*l)
##    m=m+2
##    l=l-1
##    if l<0:
##        break
##   output
##      *      
##     ***     
##    *****    
##   *******   
##  *********
##l=5
##m=1
##for w in range(5):
##    print(" "*l,"*"*m," "*l)
##    m=m+2
##    l=l-1
##    if l<0:
##        break
##l=1
##m=9
##for w in range(5):
##    print(" "*l,"*"*m," "*l)
##    m=m-2
##    l=l+1
##    if l<0:
##        break

##      *      
##     ***     
##    *****    
##   *******   
##  *********  
##  *********  
##   *******   
##    *****    
##     ***     
##      *    
l=1
for w in range (5):
    print("*"*l)
    l=l+1
    if l==5:
        for w in range(5):
            l=l-1
            print("*"*l)
            
    
    

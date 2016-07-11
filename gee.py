import random
sum=0
m=input("enter the number of rows")
n=input("enter the number of columns")
prod=m*n
var=1
a=[[0 for x in range (m)] for y in range(n)]

for x in range(0,m):
    for y in range(0,n):
        a[x][y]=var
        var+=1
        
def sum1():
    row=[0 for i in range(m)]
    col=[0 for i in range(n)]
    for i in range(m):
        row[i]=0
    for i in range(n):
        col[i]=0
        
    
    for i in range(m):
        for j in range(n):
                row[i]=row[i]+a[i][j]  
                
    for i in range(n):
        for j in range(m):             
                col[i]=col[i]+a[i][j]
         
    for i in range(m):
        if(row[i]==0):
                return False
            
    for i in range(n):
        if(col[i]==0):
                return False 
                           
    return True

while(sum1()):
    random_num=random.randrange(1,7)
    print"the value of the rolled die is",random_num
    if(sum+random_num<=prod):
        sum=sum+random_num
    else:
        sum=sum+random_num-prod    
    
    x=sum%n
    y=sum/n
    
    if(y%2==1):
        x=n-1-x
    #if(sum==prod):
       #y=0
    
    print x,":",y    
    a[y][x]=0     
    print "sum=",sum
    print"the position of the die is (x,y)=",x,y
    for i in range(m):
        print(a[i])
    print"\n"    

print"u won! BINGO"    

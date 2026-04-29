for i in range(6):
    for j in range(7):
        if (i==0 and j% 3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print( )


n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2* i +1):
        print("*",end=" ")
    print( )

n=5
for i in range(1,n+1):
    print(" * " * i )
n,m = input().split()
n = int(n)
m = int(m)
i = 1
x = 3
y = 0
while (i < n):
    
    print(int((m-x)/2)*"-",end="")
    print(i*".|.",end="")
    print(int((m-x)/2)*"-")
    x = x + 6
    i = i + 2
if(i == n ):
    print(int(((m-7)/2))*"-" +"WELCOME"+int(((m-7)/2))*"-" )
while (i > 1): 
    x = x - 6
    y= int(x/3)
    print(int((m-x)/2)*"-",end="")
    print(y*".|.",end="")
    print(int((m-x)/2)*"-")
    i = i - 2    
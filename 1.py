n=int(input())
s=""
l=[0,1,2]
while True:
    i=n%3
    x=str(i)
    s+=x
    n=n/3
    if n in l:
        x=str(n)
        s+=x
        break 
print(s)       

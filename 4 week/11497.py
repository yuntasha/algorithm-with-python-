import sys

a=int(sys.stdin.readline())

for _ in range(a):
    n=int(sys.stdin.readline())
    b=sorted(list(map(int,sys.stdin.readline().split(" "))),reverse=True)
    max=0
    k=[]
    for j in range(n):
        if j%2==0:
            k.append(b.pop(0))
        else:
            k.insert(0,b.pop(0))
    F=k[0]
    max=0      
    for i in k:
        L=F
        F=i
        
        if max<abs(L-F):
            max=abs(L-F)
    print(max)
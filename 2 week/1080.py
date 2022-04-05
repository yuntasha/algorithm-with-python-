n,m=map(int,input().split(" "))

a=str(input())
b=str(input())

c1=[]
c2=[]

for i in range(n):
    if a[i]==b[i]:
        c1.append(0)
        c2.append(0)
    else:
        c1.append(1)
        c2.append(1)
cnt1=0
cnt2=1
one=0
result=0
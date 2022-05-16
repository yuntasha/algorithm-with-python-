import sys

n=int(sys.stdin.readline())

array=sorted(list(map(int,sys.stdin.readline().split())))
max=array.pop()
min=array.pop(0)
minn=min
maxn=max
tmp=min+max
result=abs(tmp)
while array:
    if tmp>0:
        max=array.pop()
    else:
        min=array.pop(0)
    tmp=min+max
    if abs(tmp)<result:
        result=abs(tmp)
        maxn=max
        minn=min
        
print(minn,maxn)
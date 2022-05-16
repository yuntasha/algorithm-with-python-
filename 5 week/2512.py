import sys

n=int(sys.stdin.readline())

array = list(map(int,sys.stdin.readline().split()))

m=int(sys.stdin.readline())
start=1
end=max(array)

result=0
while start<=end:
    total=0
    mid=(start+end)//2
    for x in array:
        if x>=mid:
            total+=mid
        else:
            total+=x
            
    if total > m:
        end=mid-1
    else:
        result=mid
        start=mid+1
        
print(result)
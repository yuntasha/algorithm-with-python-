import sys

n=int(sys.stdin.readline())

arr=sorted(list(map(int,sys.stdin.readline().split())))

right=n-1
left=0
a,b=arr[right],arr[left]
tot=abs(arr[right]+arr[left])

while right>left:
    if tot>abs(arr[right]+arr[left]):
        a,b=arr[right],arr[left]
        tot=abs(arr[right]+arr[left])
    if arr[right]+arr[left]<0:
        left+=1
    else:
        right-=1

if a>b:
    print(b,a)
else:
    print(a,b)
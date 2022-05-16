import sys

n=int(sys.stdin.readline())
for _ in range(n):
    an=int(sys.stdin.readline())
    a=[]
    for _ in range(an):
        a.append(list(map(int,sys.stdin.readline().split(" "))))
    a.sort()
    min=a[0][1]
    cnt=1
    for k in range(1,an):
        if min>a[k][1]:
            cnt+=1
            min=a[k][1]
    print(cnt)
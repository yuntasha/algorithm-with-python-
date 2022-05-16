import sys

n=int(sys.stdin.readline())
for _ in range(n):
    an, bn=map(int,sys.stdin.readline().split(" "))
    a=list(map(int,sys.stdin.readline().split(" ")))
    b=list(map(int,sys.stdin.readline().split(" ")))
    a.sort()
    b.sort()
    cnt=0
    for am in a:
        for bm in b:
            if am<=bm:
                break
            cnt+=1
    print(cnt)
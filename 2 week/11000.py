import sys

n=int(input())
k=[]
for i in range(n):
    startT,endT=map(int,sys.stdin.readline().split(" "))
    k.append([startT,1])
    k.append([endT,-1])

cnt=0
maxcnt=0
k.sort(key=lambda x:x[1])
k.sort(key=lambda x:x[0])

for i in range(2*n):
    cnt+=k[i][1]
    if maxcnt<cnt:
        maxcnt=cnt
print(maxcnt)
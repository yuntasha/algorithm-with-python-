
import sys
from bisect import bisect_left, bisect_right

N, H=map(int,sys.stdin.readline().split())

high=[]
low=[]

for _ in range(N//2):
    low.append(int(sys.stdin.readline()))
    high.append(int(sys.stdin.readline()))

low.sort()
high.sort()
total=[]
for i in range(H):
    n=i+1
    a=bisect_left(low,n)
    b=bisect_left(high,H-n+1)
    total.append(N-a-b)
    
total.sort()
print(total[0],bisect_left(total,total[0]+1))
#총 10M이라고 치자 10가지가 있음
#아래 3은 3까지 안걸림
#위에 3은 8까지
#10 1 9 2 8 3
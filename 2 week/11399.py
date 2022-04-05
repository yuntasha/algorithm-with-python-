n=int(input())

time=[]

time=list(map(int,input().split(" ")))

time.sort()

timecount=0
for i in range(n):
    timecount+=time[i]*(n-i)
    
print(timecount)
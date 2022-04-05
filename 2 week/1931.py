n=int(input())
time=[]
for i in range(n):
    time.append(list(map(int,input().split(" "))))
cnt=1
time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])
last=time[0][1]

for j in range(1,n):
    if time[j][0]>=last:
      cnt+=1  
      last=time[j][1]
        
print(cnt)
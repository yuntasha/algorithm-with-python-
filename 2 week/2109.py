n=int(input())
sum_s = 0
dp=[]
pd=[]
for _ in range(n):
    pd.append(list(map(int,input().split(" "))))

pd.sort(key = lambda x :x[1])
pd.sort(key = lambda x :x[0],reverse=True)
day=[]
for i in range(n):
    day.append([0,0])

for i in range(n):
    p=pd[i][0]
    d=pd[i][1]-1
    x=d
    if(x>=n):
        x=n-1
    while x>=0:
        if day[x][1]==0:
            day[x][0]=p
            day[x][1]=1
            break
        else:
            x-=1
for i in range(n):
    sum_s+=day[i][0]
print(sum_s)

#1-20
#2-100
#3-10
#
#
#6-5
#7-50
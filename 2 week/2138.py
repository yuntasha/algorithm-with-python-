import sys

n=int(input())

a=str(input())
b=str(input())

c1=[]
c2=[]

for i in range(n):
    if a[i]==b[i]:
        c1.append(0)
        c2.append(0)
    else:
        c1.append(1)
        c2.append(1)
cnt1=0
cnt2=1
one=0
result=0

#c1은 첫 번째 안하기
#c2는 첫 번째 하기
if n==2:
    sum=c1[0]+c1[1]
    if sum==0:
        result=0
    elif sum==1:
        result=-1
    else:
        result=1
elif n==3:
    sum=c1[0]+c1[1]+c1[2]
    if sum==3:
        result=1
    elif sum==2:
        if c1[1]==1:
            result=1
        else:
            result=2
    elif sum==1:
        if c1[1]==1:
            result=3
        else:
            result=2
    else:
        result=0
else:
    for i in range(2):
        c2[i]=(c2[i]+1)%2#앞에꺼 2개 바꿔줌
    for i in range(n-2):#마지막꺼 포함 x 현재거부터 3개
        if c1[i]==1:
            c1[i]=(c1[i]+1)%2
            c1[i+1]=(c1[i+1]+1)%2
            c1[i+2]=(c1[i+2]+1)%2
            cnt1+=1
        if c2[i]==1:
            c2[i]=(c2[i]+1)%2
            c2[i+1]=(c2[i+1]+1)%2
            c2[i+2]=(c2[i+2]+1)%2
            cnt2+=1
    if c1[n-2]+c1[n-1]==1:
        cnt1=-1
    elif c1[n-2]+c1[n-1]==2:
        cnt1+=1
    
    if c2[n-2]+c2[n-1]==1:
        cnt2=-1
    elif c2[n-2]+c2[n-1]==2:
        cnt2+=1
    
    if cnt1==-1 and cnt2==-1:
        result=-1
    elif cnt1==-1 or cnt2==-1:
        result=cnt1+cnt2+1
    else:
        if cnt1>cnt2:
            result=cnt2
        else:
            result=cnt1
print(result)
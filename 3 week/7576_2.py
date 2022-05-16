from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())

miro=[]

xq=deque()
yq=deque()

for i in range(m):
    miro.append(list(map(int,sys.stdin.readline().split(" "))))
    for j in range(n):
        if miro[i][j]==1:
            xq.append(i)
            yq.append(j)
    
dx=[0,1,0,-1]
dy=[1,0,-1,0]



def BFSmiro():
    max=0
    while xq:
        x=xq.popleft()
        y=yq.popleft()
        
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            
            if xx<0 or xx==m or yy<0 or yy==n:
                continue
            if miro[xx][yy]==0 or miro[x][y]<miro[xx][yy]:
                miro[xx][yy]=miro[x][y]+1
                xq.append(xx)
                yq.append(yy)
                if max<miro[xx][yy]:
                    max=miro[xx][yy]
    return max

max=BFSmiro()

if max!=-1:
    max-=1
print(max)

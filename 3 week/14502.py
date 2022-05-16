from collections import deque

n, m = map(int,input().split())

miro=[]

for _ in range(n):
    miro.append(list(map(int,input())))
    
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def BFSmiro(x,y):

    xq=deque()
    yq=deque()
    xq.append(x)
    yq.append(y)
    while xq:
        x=xq.popleft()
        y=yq.popleft()
        
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            
            if xx<0 or xx==n or yy<0 or yy==m:
                continue
            if miro[xx][yy]==0:
                miro[xx][yy]=2
                xq.append(xx)
                yq.append(yy)


def makewall(x,y,cnt):
    if cnt==3:
        for i in range(n):
            for j in range(m):
                
N, L=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
a.sort()
b=a.pop(0)
cnt=1
while a:
    c=b
    b=a.pop(0)
    if b-c>=L:
        cnt+=1
    else:
        b=c
        
print(cnt)
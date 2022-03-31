import sys

n=int(sys.stdin.readline())
stack=list()
top=-1
for _ in range(n):
    a=list(map(str,sys.stdin.readline().strip().split(" ")))
    if a[0]=="push":
        stack.append(int(a[1]))
        top+=1
    elif a[0]=="pop":
        if top==-1:
            print("-1")
        else:
            b=stack.pop()
            top-=1
            print(b)
    elif a[0]=="size":
        print(top+1)
    elif a[0]=="empty":
        if top==-1:
            print("1")
        else:
            print("0")
    elif a[0]=="top":
        if top==-1:
            print("-1")
        else:
            print(stack[-1])
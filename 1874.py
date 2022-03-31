kkkk=int(input())
data=list()
for i in range(kkkk):
    data.append(i+1)
stack=list()
pdata=list()

for _ in range(kkkk):
    p=int(input())
    pdata.append(p)
#pdata에 목표하는 수리스트가 있고 data->stack
pri=list()
last=1
tf=0
for _ in range(kkkk): #각 수를 스택에 넣었다 빼면서 만듦
    num=pdata.pop(0)#end에 넣을 목표 숫자를 꺼냄
    while num>=last:
        stack.append(last)
        pri.append("+")
        last+=1
    ldata=stack.pop()
    if ldata==num:
        pri.append("-")
    else:
        tf=1
        break
        
if tf==1:
    print("NO")
else:
    for ynumb in pri:
        print(ynumb)
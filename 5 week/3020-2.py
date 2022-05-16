import sys
N, H=map(int,sys.stdin.readline().split())

top=[]
bot=[]

for _ in range(N//2):
    bot.append(int(sys.stdin.readline()))
    top.append(int(sys.stdin.readline()))

sorted(top,reverse=True)
sorted(bot,reverse=True)

#찾아가는건 동빈나씨가 해놓은 왼쪽부터 하는걸로 몇번째 인덱스에 들어가야
#되는지 아는걸로 몇개가 필요한지 찾아가는 것
#위아래로 더 빠르게 사라지고 추가되는 것으로 가봐야할듯?
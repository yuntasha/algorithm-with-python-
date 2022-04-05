import sys

kind, money=map(int,input().split(" "))

count=0

coin=list()

for _ in range(kind):
    k=int(input())
    coin.append(k)

while money!=0:
    y=coin.pop()
    count+=money//y
    money=money%y

print(count)
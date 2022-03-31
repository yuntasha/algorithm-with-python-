import heapq
import sys

howmany=int(sys.stdin.readline())
heap = []
for _ in range(howmany):
    n=int(sys.stdin.readline())
    if n==0:
        if not heap:
            print("0")
        else:
            k=heapq.heappop(heap)
            print(k)
    else:
        heapq.heappush(heap,n)
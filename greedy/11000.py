import sys
import heapq

n = int(sys.stdin.readline())
cls = []
for _ in range(n):
    cls.append(list(map(int, sys.stdin.readline().split())))
cls.sort(key=lambda x: (x[0], x[1]))

h = []
heapq.heappush(h, cls[0][1]) # 처음 강의의 종료시간 넣어줌
for i in range(1, n):
    if cls[i][0] >= h[0]:   # 한 강의실에서 계속 진행 가능
        heapq.heappop(h)
        heapq.heappush(h, cls[i][1])
    else:   # 새로운 강의실 배정
        heapq.heappush(h, cls[i][1])
print(len(h))
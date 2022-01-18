import heapq

n, k, s = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
h1, h2 = [], []
for x in array:
    if x[0] < s:
        heapq.heappush(h1, [-(s - x[0]), x[1]])  # 학교보다 왼쪽에 위치
    else:
        heapq.heappush(h2, [-(x[0] - s), x[1]])  # 학교보다 오른쪽에 위치

def func(h):
    result = 0  # 총 이동거리
    count = 0   # 버스인원
    distance = 0    # 학교로 돌아올때까지 한번의 이동거리

    while h:
        dist, c = heapq.heappop(h)  # 학교와의 거리, 아파트 인원수
        if distance == 0:
            distance = -(dist*2)    # 아파트까지의 거리를 총 이동거리에 더해줌
            result += distance

        if count + c > k:   # 아파트의 모두를 태웠을때 정원초과인경우
            c -= (k - count)    # 태울수 있는 만큼 태우고
            count = 0   # 다시 학교로 돌아간다
            distance = 0
            heapq.heappush(h, [dist, c])    # 다시 힙에 넣어준다
        else:   # 모두 태울 수 있는경우
            count += c  # 버스에 모두 태운다
    return result

print(func(h1) + func(h2))
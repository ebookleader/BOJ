from collections import deque
def bfs(numbers, target):
    queue = deque()
    queue.append([0, numbers[0]])
    queue.append([0, -1 * numbers[0]])
    ans = 0
    l = len(numbers) - 1
    while queue:
        idx, t = queue.popleft()
        if idx == l:
            if t == target:
                ans += 1
        elif idx < l:
            queue.append([idx+1, t + numbers[idx+1]])
            queue.append([idx+1, t - numbers[idx+1]])
    return ans

def solution(numbers, target):
    return bfs(numbers, target)

print(solution([1, 1, 1, 1, 1], 3))
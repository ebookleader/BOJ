from collections import deque

def bfs(n, begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = [False] * len(words)

    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            diff = 0
            if not visited[i]:
                for x, y in zip(word, words[i]):
                    if x != y:
                        diff += 1
            if diff == 1: # 한글자만 다르면
                queue.append([words[i], cnt+1])
                visited[i] = True
    return 0

def solution(begin, target, words):
    answer = bfs(len(begin), begin, target, words)
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
def solution(n, lost, reserve):
    lst = [1] * n
    lst = [0] + lst + [0]

    for x in lost:
        lst[x] -= 1
    for x in reserve:
        lst[x] += 1

    for i in range(n, 0, -1):
        if lst[i] == 0:
            if lst[i+1] == 2:
                lst[i+1] -= 1
                lst[i] += 1
            elif lst[i-1] == 2:
                lst[i-1] -= 1
                lst[i] += 1
    return n - (lst.count(0)) + 2

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(3, [3], [1]))
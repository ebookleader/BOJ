def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    return ''.join(stack[:len(number)-k])

print(solution("4177252841", 4))
print(solution("1111111", 3))
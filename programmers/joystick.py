def solution(name):
    lst = []
    for word in name:
        up = ord(word) - 65
        down = 25 - up + 1
        lst.append(min(up, down))
    # right
    right = 0
    for i in range(len(name)):
        if i == (len(name)-1):
            if name[i] == 'A':
                right -= 1
            right += lst[i]
        else:
            right += lst[i]
            right += 1
    # left
    left = lst[0] + 1
    for j in range(len(name)-1, 0, -1):
        if j == 1:
            if name[j] == 'A':
                left -= 1
            left += lst[j]
        else:
            left += lst[j]
            left += 1
    return min(left, right)

# print(solution("JEROEN"))
# print(solution("JAZ"))
# print(solution("JAN"))
print(solution("ABAAAAAAAAABB"))
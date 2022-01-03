import sys

def function(dna_list, n, m):
    result = ''
    cnt = 0
    for i in range(m):
        dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(n):
            w = dna_list[j][i]
            dic[w] += 1

        result += max(dic, key=dic.get)
        cnt = cnt + (n - max(dic.values()))
    print(result)
    print(cnt)
    return

n, m = map(int, sys.stdin.readline().split())
dna_list = []
for _ in range(n):
    dna_list.append(sys.stdin.readline().rstrip())
function(dna_list, n, m)

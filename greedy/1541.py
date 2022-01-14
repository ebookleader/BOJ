import sys

exp = sys.stdin.readline().rstrip().split('-')
result = 0
# 첫번째 원소 더해주기
for x in exp[0].split('+'):
    result += int(x)
# 두번재 원소부터는 뺄셈연산
for x in exp[1:]:
    v = 0
    for y in x.split('+'):
        v += int(y)
    result -= v
print(result)
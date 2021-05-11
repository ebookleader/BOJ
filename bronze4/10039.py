import sys
lst = [int(sys.stdin.readline()) for _ in range(5)]
total = 0
for x in lst:
    if x < 40:
        x = 40
    total += x
print(total//5)
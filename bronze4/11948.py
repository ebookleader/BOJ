import sys
A,B,C,D,E,F = [int(sys.stdin.readline()) for _ in range(6)]
four = [A, B, C, D]
four.remove(min((four)))
print(sum(four) + max(E, F))
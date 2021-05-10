import sys
a, b, c = map(int, sys.stdin.readline().split())
if b >= c:
    print(-1)
else:
    # a+bx < cx
    # a < (c-b)x
    # a/(c-b) < x

    # while True:
    #     if income > 0:
    #         break
    #     cnt += 1
    #     cost += b
    #     income = c*cnt - cost
    # print(cnt)
    print(a//(c-b)+1)
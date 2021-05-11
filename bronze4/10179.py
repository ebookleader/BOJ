import sys
T = int(sys.stdin.readline())
price_list = [float(sys.stdin.readline()) for _ in range(T)]
for p in price_list:
    print('${:.2f}'.format(round(p*0.8, 2)))
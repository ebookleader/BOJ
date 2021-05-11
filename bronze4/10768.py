import sys
month = int(sys.stdin.readline())
day = int(sys.stdin.readline())
if month == 2:
    if day == 18:
        print('Special')
    elif day < 18:
        print('Before')
    else:
        print('After')
elif month < 2:
    print('Before')
else:
    print('After')
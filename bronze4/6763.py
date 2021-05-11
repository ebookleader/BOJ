import sys
limit = int(sys.stdin.readline())
speed = int(sys.stdin.readline())
if speed <= limit:
    print('Congratulations, you are within the speed limit!')
else:
    fine = 0
    diff = speed - limit
    if diff <= 20:
        fine = 100
    elif diff >= 31:
        fine = 500
    else:
        fine = 270
    print(f'You are speeding and your fine is ${fine}.')
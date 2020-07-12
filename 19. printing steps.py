for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

# 별로 사각형 그리기
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

# 계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

# 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

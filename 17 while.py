import random

i = 10
while i > 0:
    print('Hello, world', i)
    i -= 1

print(random.randint(1, 6))

i = 0
while i != 3:    # 3이 아닐 때 계속 반복
    i = random.randint(1, 6)    # randint를 사용하여 1과 6 사이의 난수를 생성
    print(i)

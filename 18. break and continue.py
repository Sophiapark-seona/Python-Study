for i in range(100):
    if i % 2 == 0:
        continue
    print(i) # 홀수만 출력


count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break

i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1
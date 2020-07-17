for i in range(1, 101):
    if i % 15 == 0: # 만약 i가 30인데 3의 배수를 먼저 검사하면 Fizz 출력되므로 공배수먼저 검사해야 함
        # i % 3 == 0 and i % 5 == 0 처럼 의미를 명확하게 드러내는게 더 좋음
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
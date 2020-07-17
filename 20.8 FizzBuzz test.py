num1, num2 = map(int, input().split())

for i in range(num1, num2+1):
    if i % 5 == 0 and i % 7 ==0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
a = list(map(int, input().split()))
num1, num2 = a

a = [2 ** i for i in range(num1, num2 + 1)]

del a[1]
del a[-2]

print(a)
import string

text = input()

textsplit = text.split(' ')

count = 0
for i in textsplit:
    if i.strip('.,') == 'the':
        count += 1


print(count)
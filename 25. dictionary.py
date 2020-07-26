#x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
#x.setdefault('e')
#x.setdefault('f', 100)
#x.update(a=90)
#x.update(e=50)
#x.update(a=900, f=60)
#print(x)

#y = {1: 'one', 2: 'two'}
#y.update({1: 'ONE', 3: 'THREE'})
#y.update([[2, 'TWO'], [4, 'FOUR']])
#y.update(zip([1, 2], ['one', 'two']))
#print(y)

#print(x.get('a'))

#x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
#print(x.items())
#print(x.keys())
#print(x.values())

#keys = ['a', 'b', 'c', 'd']
#x = dict.fromkeys(keys, 100)
#print(x)


#x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
#for key, value in x.items():
#    print(key, value)

#for key, value in {'a': 10, 'b': 20, 'c': 30}.items():
#    print(key, value)


#keys = ['a', 'b', 'c', 'd']
#x = {key: value for key, value in dict.fromkeys(keys).items()}
#print(x)


maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)
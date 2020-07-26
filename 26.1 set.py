a = set('apple')
#print(a)

b = set(range(5))
#print(b)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
#print(a | b)
#print(set.union(a, b))
#print(a & b)
#print(set.intersection(a,b))
#print(a - b)
#print(set.difference(a, b))
#print(a ^ b)


a = {1, 2, 3, 4}
a |= {5}
print(a)
a.update({6})
print(a)
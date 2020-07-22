#print('Hello, world!'.replace('world', 'Python'))


#table = str.maketrans('aeiou', '12345')
#a = 'apple'.translate(table)
#print(a)


#b = 'apple, pear, grape, pineapple, orange'.split(', ')
#print(b)

#d = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
#print(d)

#e = 'python'.upper()
#print(e)


#print('     python    '.lstrip())
#print('     python    '.rstrip())
#print('     python    '.strip())
#print(', python.'.lstrip(','))
#print(', python. '.strip(',.')) #It don't delete '.'
#print(', python.'.strip(',.')) #It delete '.'


#import string
##print(', python.'.strip(string.punctuation))
#print(', python.'.strip(string.punctuation + ' '))
#print(', python.'.strip(string.punctuation).strip())


#print('python'.rjust(10))
#print('python'.center(10))


#print('python'.rjust(10).upper())


#print('35'.zfill(4))
#print('3.5'.zfill(6))
#print('hello'.zfill(10))

#print('apple pineapple'.find('pl'))

#print('apple pineapple'.rfind('pl'))

#print('I am %s' % 'james')
#name = 'maria'
#print('I am %s.' % name)
#print('%.2f' % 2.3)

#print('%10s' % 'python')

#print('%10.2f' % 2.3)
#print('%10.2f' % 2000.3)
#print('%-10.2f' % 2.3)

#print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))

#print('Hello, {language} {version}'.format(language='Python', version=3.6))

#language = 'Python'
#version = 3.6
#print(f'Hello, {language} {version}')

#print('{0:>10}'.format('Python'))

#print('{0:03d}'.format(35))
#print('%08.2f' % 3.6)
#print('{0:08.2f}'.format(150.37))
#print('{0:x>10}'.format(15))

print(format(148749345,','))

print('%20s' % format(454222344, ','))
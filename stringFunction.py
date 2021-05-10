python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())  # python의 0번째 요소가 대문자니?
print(len(python))  # length of string
print(python.replace('Python', 'Java'))

index = python.index('n')  # location of 'n'
print(index)
# index+1 is start point, default return is error
index = python.index('n', index+1)
print(index)

print(python.find('n'))
print(python.find('java'))  # default retrun is -1
print('hi')

print(python.count('n'))  # how many time 'n' in string

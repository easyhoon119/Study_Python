# {key : value}
cabinet = {3: '유재석', 100: '김태호'}
print(cabinet)
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) : syntax error
print(cabinet.get(5))  # default value is 'none'
print(cabinet.get(5, '사용가능'))  # alternate text
print(cabinet)

# in operator
print(3 in cabinet)  # ture
print(5 in cabinet)  # false

cabinet = {'A-3': '유재석', 'B-100': '김태호'}
print(cabinet['A-3'])
print(cabinet)
cabinet['A-3'] = '김종국'  # update dictionary
cabinet['C-20'] = '조세호'  # add dictionary
print(cabinet)

del cabinet['A-3']  # delete dicitonary
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)

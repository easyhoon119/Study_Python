print('a'+'b')
print('a', 'b')

# 방법 1
print('나는 %d살 입니다.' % 20)
print('나는 %s을 좋아해요.' % '파이썬')
print('APPLE 은 %c로 시작해요.' % 'A')
# %s는 타입과 상관없이 STring으로 변환해준다.
print('나는 %s색과 %s색을 좋아해요.' % ('파란', '빨간'))

# 방법 2
print('나는 {}살 입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파랑', '노랑'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파랑', '노랑'))  # numbering

# 방법 3
print('나는 {age}살이며 {color}색을 좋아해요.'.format(age=20, color='빨간'))
print('나는 {color}살이며 {age}색을 좋아해요.'.format(age=20, color='빨간'))
age = 40
color = '노랑'
print('나는 {age}살이며 {color}색을 좋아해요.'.format(age=age, color=color))

# 방법 4(python 3.6이상~)
age = 20
color = '빨간'
print(f'나는 {color}살이며 {age}색을 좋아해요.')

# escape character
print('백문이 불여일견\n백견이 불여일타')  # new line
print('저는 "나도코딩" 입니다')  # print '""'
print("저는 \"나도코딩\" 입니다.")
print('c:\\users\\desk\\python')  # print '\'
# \r : 커서를 맨앞으로 이동
# \t : equal ketboard 'tab'
# \b : equal keyboard 'backspace'

# Quiz 3
url = 'http://naver.com'
password = url.replace('http://', '')
print(password)
password = password[:password.index('.')]
print(password)
password = password[:3] + str(len(password)) + str(password.count('e')) + '!'
print('생성된 비밀번호 : '+password)
print('{0}의 비밀번호는 {1} 입니다.'.format(url, password))

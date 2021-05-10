# for loop
# 1. for in loop
from random import *
for wating_no in [0, 1, 2, 3, 4]:
    print('대기번호 : {0}'.format(wating_no))

for wating_no in range(1, 6):
    print('대기번호 : {0}'.format(wating_no))

starbucks = ['아이언맨', '토르', '아이엠 구르트']
for customer in starbucks:
    print('{0}님 커피가 준비되어씃ㅂ니다.'.format(customer))

# 1 line for loop
stdents = [1, 2, 3, 4, 5]
stdents = [i+100 for i in stdents]
print(stdents)
stdents = ['iron man', 'thor', 'i am groot']
stdents = [len(i) for i in stdents]
print(stdents)
stdents = ['iron man', 'thor', 'i am groot']
stdents = [i.upper() for i in stdents]
print(stdents)

# while loop
customer = '토르'
index = 5
while index >= 1:
    print('{0}, 커피가 준비 되었습니다. {1}번 남았습니다.'.format(customer, index))
    index -= 1
    if index == 0:
        print('커피가 폐기처분 되었습니다.')

customer = '아이언맨'
index = 1
while True:
    print('{0}, 커피가 준비 되었습니다. 호출 {1}회'.format(customer, index))
    index += 1
    if index > 3:
        break

customer = '토르'
person = 'Unknown'

while person != customer:
    print('{0}, 커피가 준비 되었급니다.'.format(customer))
    person = input('이름이 어떻게 되세요?')

# continue & break
# continue : go condition state
# break : go outside of loop state
absent = [2, 5]
nobook = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in nobook:
        print('오늘 수업은 여기까지 {0}은 교무실로 따라와'.format(student))
        break
    print('{0}야 책을 읽어봐'.format(student))

# Quiz 5
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print('[0] {0}번째 손님 (소요시간 : {1}분)'.format(i, time))
        cnt += 1
    else:
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i, time))
print('총 탑승 승객 : {0}분'.format(cnt))

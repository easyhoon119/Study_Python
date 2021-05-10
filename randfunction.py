from random import *

print(random())  # 0.0 ~ 1.0 among value not contain 1.0
print(random() * 10)  # 0.0 ~ 10.0  among value not contain 10.0
print(int(random()*10))  # int typecast 0 ~ 10 among value not contain 10
print(int(random()*10) + 1)  # 1~11 among value not contain 11

print(int(random()*45) + 1)  # 1 ~ 46 aomng value not contain 46
print(randrange(1, 46))  # 1 ~ 45 among value
print(randint(1, 45))  # 1 ~ 45 among value

# Quiz 2
studyDate = randint(4, 28)
print('오프라인 스터디 모임의 날짜는 매월 ' + str(studyDate)+'일로 선정되엇습니다.')

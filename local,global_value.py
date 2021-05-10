gun = 10


def checkpoint(soldiers):
    global gun  # 전역 공간에 있는 GUN 사용
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))
    return gun


print('전체 총 : {0}'.format(gun))
checkpoint(2)
print('남은 총 : {0}'.format(gun))
gun = checkpoint_ret(gun, 2)
print('남은 총 : {0}'.format(gun))

# Quiz 6


def std_weight(height, gender):
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21


height = 1.75
gender = '남자'
standard = std_weight(height, gender)
print('키 {0}cm {2}의 표준 체중은 {1}kg 입니다.'.format(
    int(height*100), round(standard, 2), gender))

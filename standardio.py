import sys
print('python', 'java', 'javascript', sep=' vs ')  # 분리할 문자 추가
print('python', 'java', 'javascript', end='?')  # 마지막에 추가할 문자 추가
print('무엇이 더 재밌을까요?')

print('python', 'java', file=sys.stdout)
print('python', 'java', file=sys.stderr)  # error check

scores = {'수학': 0, '영어': 50, '코딩': 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=':')

# 은행 대기 순번표
for num in range(1, 21):
    print('대기번호 : ' + str(num).zfill(3))  # 없는공간은 0으로 채우기

answer = input('아무값이나 입력하세요 : ')  # input은 무조건 String 으로 받는다
print(type(answer))
print("입력한 값은" + answer + '입니다.')

# output format
print('{0: > 10}'.format(500))  # 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 확보
# 양수일 땐 +로 표시, 음수 일땐 -로 표시
print('{0: >+10}'.format(-500))
print('{0: >+10}'.format(500))
# 왼쪽 정렬을 하고, 빈칸으로, _로 채움
print('{0:_<10}'.format(500))
# 3자리마다 , 직어주기
print('{0:,}'.format(10000000000000))
print('{0:+,}'.format(10000000000000))
# 3자리마다 ,를 찍어주기, 부호도 붙이고, 자리수 확보하기, 빈자리는 ^로 채워주기
print('{0:^<+30,}'.format(1000000000000))
# 소수점 출력
print('{0:.3f}'.format(5/3))

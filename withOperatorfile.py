# 자동으로 close를 해준다!
import pickle

with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))

# with open('study.txt', 'w', encoding='utf8') as study_file:
#     study_file.write('파이썬을 열심히 공부하고 있습니다.')

with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())


# Quiz 7
for i in range(1, 5):
    with open(str(i)+'주차.txt', 'w', encoding='utf8') as report_file:
        report_file.write('- ' + str(i) + ' 주차 주간보고 -')
        report_file.write('\n부서 : ')
        report_file.write('\n이름 : ')
        report_file.write('\n업무 요약 : ')

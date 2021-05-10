# input
# lang = input('무슨 언어를 좋아하세요?')
# print('{0}은 아주 좋은 언어 입니다.'.format(lang))

# dir: 객체가 넘겨 졌을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# import random
# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))
# name = 'Jim'
# print(dir(name))

# outer funtion
# glob : 경로내의 폴더/ 파일을 조회
# import glob
# print(glob.glob('*.py'))  # 확장자가 py인 모든 파일
# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd)  # 현재 디렉토리출력
# folder = 'sample_dir'
# if os.path.exists(folder):
#     print('이미 존재하는 폴더입니다.')
#     os.rmdir(folder)  # remove folder
#     print(folder, '폴더를 삭제했습니다.')
# else:
#     os.makedirs(folder)  # create folder
#     print(folder, '폴더를 생성했습니다.')
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

# import datetime
# # print('오늘 날짜는 ', datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days=100)  # 100일을 저장
# print('우리가 만난지 100일은', today + td)  # 오늘 부터 백일 후

# Qiuz 10
import byme_module as byme
byme.sign()

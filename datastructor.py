# 자료구조의 변형
from random import *
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# Quiz4
first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# first = range(1, 21) # 1부터 20까지 숫자를 생성
#first = list(first)
chiken = []
coffee = []
shuffle(first)
winners = sample(first, 4)
print('--당첨자 발표--')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print('--축하합니다--')

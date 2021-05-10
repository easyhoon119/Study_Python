sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """ 
나는 소년이고,
파이썬은 귀워요
"""  # multi sentence
print(sentence3)

# slicing string
jumin = "970711 1851910"
print("성별 : " + jumin[7])
print('연 : ' + jumin[0:2])  # 0~2 직잔까지의 값
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])
print('생년월일 : ' + jumin[:6])  # 0 부터 6 직전까지의 값
print('뒤 7자리 : ' + jumin[7:])  # 7 부터 마지막까지의 값
print('뒤 7자리 (뒤에서부터) : ' + jumin[-7:])  # 뒤에서부터 7번째 부터 마지막까지의 값

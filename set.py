#집합(set), 중복안됨, 순서없음
myset = {1, 2, 3, 3, 5}  # 중복은 무시한다
print(myset)

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 파이썬을 할줄아는 사람이 늘어났다
python.add('김태호')
print(python)

# java를 까먹었다.
java.remove('김태호')
print(java)

num_set1 = {1, 2, 4, 5, 6, 1}
num_set2 = {2, 4, 5, 5, 8, 9}
print(num_set1 & num_set2)
print(num_set1 and num_set2)
print(num_set1 or num_set2)
print(num_set1 | num_set2)

# [] : 순서를 가진 객체의 집합
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "빅명수"]
print(subway)
print(subway.index('조세호'))
subway.append('하하')  # add list
print(subway)
subway.insert(1, '정형돈')  # add list specific seat
print(subway)
subway.pop()  # delete list from last
print(subway)
# subway.pop()  # delete list from last
# print(subway)
# subway.pop()  # delete list from last
# print(subway)
subway.append('유재석')
print(subway.count('유재석'))

num_list = [5, 6, 3, 8, 3, 9]
num_list.sort()  # sorting 작은값부터
print(num_list)
num_list.reverse()  # 뒤집기
print(num_list)
num_list.clear()  # remove list all
print(num_list)

# 다양한 자료형과 함께 사용(dinamic)
num_list = [5, 6, 3, 8, 3, 9]
mix_list = ['조세호', 30, True]
print(mix_list)
num_list.extend(mix_list)  # list 합치기
print(num_list)

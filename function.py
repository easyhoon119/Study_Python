def open_account():
    print('새로운 계좌가 생성되었습니다.')


open_account()

# return, parameter


def deposit(balance, money):
    print('입금이 완료 되엇습니다. 잔액은 {0} 원 입니다.'.format(balance+money))
    return balance+money


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료 됬습니다. 잔액은 {0} 원 입니다.".format(balance-money))
        return balance - money
    else:
        print('출금이 완료되지 않앗습니다. 잔액은 {0} 원 입니다.'.format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money-commission  # return tuple format


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 400)
print(balance)
print('수수료 {0} 원이며, 잔액은 {1} 원 입니다.'.format(commission, balance))

# default value


def profile(name, age, main_lang):
    print('이름  : {0},  나이 : {1},  주 사용 언어 : {2}'.format(name, age, main_lang))


profile('유재석', 20, '파이썬')
profile('김태호', 25, '자바')

# default 지정하기


def profile2(name, age=17, main_lang='파이썬'):
    print('이름  : {0},  나이 : {1},  주 사용 언어 : {2}'.format(name, age, main_lang))


profile2('유재석')
profile2('김태호')

# funtion with keyword value


def profile3(name, age, main_lang):
    print(name, age, main_lang)


profile3(name='유재석', main_lang='파이썬', age=20)
profile3(main_lang='자바', age=25, name='김태호')


# 가변인자
# def profile4(name, age, lan1, lan2, lan3, lan4, lan5):
#     print('이름 : {0}, 나이 : {1}, '.format(name, age), end=" ")
#     print(lan1, lan2, lan3, lan4, lan5)

def profile4(name, age, *language):
    print('이름 : {0}, 나이 : {1}, '.format(name, age), end=" ")
    for lan in language:
        print(lan, end=" ")
    print()


profile4('유재석', 20, 'python', 'java', 'c', 'c++', 'c#')
profile4('김태호', 25, 'kotlin', 'swift')

from random import *


class Unit:
    def __init__(self, name, hp, speed):  # 필수 생성자 무조건 집어넣자
        self.name = name  # member valuable
        self.hp = hp
        self.speed = speed
        print('{0} 유닛이 생성 되었습니다.'.format(name))
        # self.damage = damage
        # print('{0} 유닛이 생성 되었습니다.'.format(self.name))
        # print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(
            self.name, location, self.speed))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.')


class AttackUnit(Unit):  # inheritence
    def __init__(self, name, hp, speed, damage):  # 필수 생성자 무조건 집어넣자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):  # method
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(
            self.name, location, self.damage))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def steampack(self):
        if self.hp > 10:
            self.hp -= 10
            print('{0} : 스팀팩을 사용합니다. (HP 10 감소)'.format(self.name))
        else:
            print('{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.'.format(self.name))


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self,):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print('{0} : 시즈모드로 전환합니다.'.format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print('{0} : 시즈모드로 해제합니다.'.format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(
            name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # method overloading
        print('[공중 유닛 이동]')
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print('{0} : 클로킹 모드 해제합니다.'.format(self.name))
            self.clocked = False
        else:
            print('{0} : 클로킹 모드 설정합니다.'.format(self.name))
            self.clocked = True


def game_start():
    print('[알림] 새로운 게임을 시작 합니다.')


def game_over():
    print('player : gg')
    print('[player] 님이 게임에서 퇴장하셨습니다.')


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# move
for unit in attack_units:
    unit.move('1시')

# seize mod
Tank.seize_developed = True
print('[알림] 탱크 시즈모드 개발이 완료 되었습니다.')

# prepare the attack
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.steampack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# attack
for unit in attack_units:
    unit.attack('1시')

# damaged
for unit in attack_units:
    unit.damaged(randint(5, 21))

# game over
game_over()

# Quiz 8


class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print('{0} {1} {2} {3} {4}'.format(self.location, self.house_type,
                                           self.deal_type, self.price, self.completion_year))


h1 = House('강남', '아파트', '매매', '10억', '2010년')
h2 = House('마포', '오피스텔', '전세', '5억', '2007년')
h3 = House('송파', '빌라', '월세', '500/50', '2000년')
house = []
house.append(h1)
house.append(h2)
house.append(h3)

print('총 {0}대의 매물이 있습니다.'.format(len(house)))
for home in house:
    home.show_detail()

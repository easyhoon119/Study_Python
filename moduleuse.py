# import prac_module
# prac_module.price(3)  # 3명 일반가격
# prac_module.price_morning(4)  # 4명 조조할인
# prac_module.price_soldier(5)  # 5명 군인 할인

# import prac_module as mv  # 별명 붙이기
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from prac_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from prac_module import price, price_morning
# price(5)
# price_morning(4)

from prac_module import price_soldier as soldier
soldier(5)

# import travelpackage.thailand
# trip_to = travelpackage.thailand.ThailandPackage()
# trip_to.detail()

# from travelpackage.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail

# from travelpackage import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#from random import *
from travelpackage import *  # 공개범위를 설정해줘야한다.__init__, __all__
# trip_to = vietnam.VietnamPackage()
# trip = thailand.ThailandPackage()
# trip_to.detail()
# trip.detail()

# file 위치 설정
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

import numpy as np
import matplotlib.pyplot as plt
from mapstate import MapState
from indicatordata import IndicatorData
import math

ms = MapState()

D = ms.countries

def get_color(value):
    """values between 0 and 1"""
    value = min(max(0,value), 1) * 510

    if value < 255:
        redValue = 255
        greenValue = math.sqrt(value) * 16
        greenValue = round(greenValue)
    else:
        greenValue = 255
        value = value - 255
        redValue = 255 - (value * value / 255)
        redValue = round(redValue)
    return '#' + f"{redValue:0{2}x}" + f"{greenValue:0{2}x}" + '44'

print(get_color(300))
for i in range(100):
    print(get_color(i/100))
# D = {u'Label1':26, u'Label2': 17, u'Label3':30}

# plt.bar(range(len(D)), list(D.values()), align='center')
# plt.xticks(range(len(D)), list(D.keys()))
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x
# ms.current_indicator.fetch_all_data()
ms.set_year('2017')
plt.bar(range(len(D)), list(D.values()), align='center', color=get_color(0.7))
plt.xticks(range(len(D)), list(D.keys()))
plt.show()



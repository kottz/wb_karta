from indicatordata import IndicatorData
from country_list import countries_for_language
import math


class MapState():

    def __init__(self, indicator):
        self.indicator = IndicatorData(indicator)
        self.date = self.indicator.end_date
        self.countries = dict.fromkeys(self.indicator.get_country_list())
        self.update_map()

    def update_map(self):
        d = self.countries
        for key in d:
            d[key] = self.indicator.get_info(key, self.date)

    def set_date(self, date):
        self.date = date
        self.update_map()

    def __str__(self):
       return 'år: ' + self.date + '\n' + str(self.countries)


    def get_color(self, value):
        """values between 0 and 1"""
        value = min(max(0,value), 1) * 510

        if value < 255:
            redValue = 255
            greenValue = math.sqrt(value) * 16
            greenValue = int(greenValue)
        else:
            greenValue = 255
            value = value - 255
            redValue = 255 - (value * value / 255)
            redValue = int(redValue)
        return '#' + f"{redValue:0{2}x}" + f"{greenValue:0{2}x}" + '00'



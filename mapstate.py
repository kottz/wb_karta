import pandas
import wbdata
from indicatordata import IndicatorData


class MapState():

    country_template = ['Sweden',
                        'Norway',
                        'Denmark',
                        'Finland',
                        'Iceland']
    def __init__(self):
        self.indicator = IndicatorData("NY.GDP.MKTP.CD")
        self.date = self.indicator.end_date
        self.countries = dict.fromkeys(self.country_template)
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

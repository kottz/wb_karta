import wbdata, datetime, pandas
from indicatordata import IndicatorData
from mapstate import MapState


# gdp = IndicatorData("NY.GDP.PCAP.PP.CD")

# print(gdp.get_start_date())
# print(gdp.get_end_date())
# print('value: ', gdp.get_info('Sweden', '2017'))

# print("Fetching data")
# gdp.fetch_all_data()
# print("data fetched")
# print('min: ', gdp.get_min_value())

mapState = MapState()
print(mapState.indicator.data)
print(mapState.indicator.data.info())
print('')
print(mapState)

# mapState.set_year('2016')

# print(mapState)
# mapState.current_indicator_data.fetch_all_data()
# print(mapState.current_indicator.get_percentage('Sweden', '2017'))
# mapState.set_year('1990')
# print(mapState)
# print(gdp.data['Central African Republic'])





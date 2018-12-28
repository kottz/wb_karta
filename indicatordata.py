import datetime
import pandas
from sqlalchemy import create_engine
from pandas_datareader import wb


class IndicatorData():

    engine = create_engine('sqlite:///cache.db')
    conn = engine.connect()

    def __init__(self, indicator):
        """Initiates with data from 2017-today"""
        engine = IndicatorData.engine
        conn = IndicatorData.conn
        self.indicator = indicator
        # Build cache if it does not already exist
        if not engine.dialect.has_table(engine, self.indicator):
            self.fetch_wbdata()
        else:
            self.data = pandas.read_sql(self.indicator, conn,
                                        index_col=['country', 'year'])

        self.start_date = self.data.unstack().columns[0][1]
        self.end_date = self.data.unstack().columns[-1][1]

    def fetch_wbdata(self):
        self.data = wb.download(indicator=self.indicator,
                                country='all',
                                start=1960,
                                end=2030).dropna()

        self.data.to_sql(self.indicator,
                         IndicatorData.conn,
                         if_exists='replace')

    def get_info(self, country, date):
        if int(date) >= int(self.start_date) and int(date) <= int(self.end_date):
            return self.data.loc[(country, date), self.indicator]
        else:
            return None

    def get_min_value(self):
        # if !self.all_data_fetched:
            # self.fetch_all_data()
        return self.data.min()

    def get_min_index(self):
        # if !self.all_data_fetched:
            # self.fetch_all_data()
        return self.data.idxmin()

    def get_max_value(self):
        # if !self.all_data_fetched:
            # self.fetch_all_data()
        return self.data.max()

    def get_max_index(self):
        # if !self.all_data_fetched:
            # self.fetch_all_data()
        return self.data.idxmin()

    def get_percentage(self, country, date):
        val = self.data[country][date]
        min_val = self.get_min_value()
        max_val = self.get_max_value()
        return (val-min_val) / (max_val-min_val)



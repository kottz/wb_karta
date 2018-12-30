import datetime
import pandas
from sqlalchemy import create_engine
from pandas_datareader import wb
import wbdata


class IndicatorData():


    def __init__(self, indicator):
        """Initiates with data from 2017-today"""
        self.indicator = indicator
        # Build cache if it does not already exist
        engine = create_engine('sqlite:///cache.db')
        conn = engine.connect()
        if engine.dialect.has_table(engine, self.indicator):
            self.data = pandas.read_sql(self.indicator, conn,
                                        index_col=['country', 'year'])
        else:
            self.data = wb.download(indicator=self.indicator,
                                    country='all',
                                    start=1960,
                                    end=2030).dropna()

            self.data.to_sql(self.indicator,
                             conn,
                             if_exists='replace')
        conn.close()

        self.start_date = self.data.unstack().columns[0][1]
        self.end_date = self.data.unstack().columns[-1][1]

    def fetch_wbdata(self):
        engine = create_engine('sqlite:///cache.db')
        conn = engine.connect()
        self.data = wb.download(indicator=self.indicator,
                                country='all',
                                start=1960,
                                end=2030).dropna()

        self.data.to_sql(self.indicator,
                         IndicatorData.conn,
                         if_exists='replace')
        conn.close()

    def get_info(self, country, date):
        if  (country, date) in self.data[self.indicator]:
            return self.data.loc[(country, date), self.indicator]
        else:
            return None

    def get_min_value(self):
        # if !self.all_data_fetched:
            # self.fetch_all_data()
        return self.data.min()[self.indicator]

    def get_min_index(self):
        # if !self.all_data_fetched:
            # self.fetch_all_data()
        return self.data.idxmin()

    def get_max_value(self):
        # if !self.all_data_fetched:
            # self.fetch_all_data()
        return self.data.max()[self.indicator]

    def get_max_index(self):
        # if !self.all_data_fetched:
            # self.fetch_all_data()
        return self.data.idxmin()

    def get_percentage(self, country, date):
        if (country, date) not in self.data[self.indicator]:
            return 0
        val = self.data.loc[(country, date), self.indicator]
        min_val = self.get_min_value()
        max_val = self.get_max_value()
        return (val-min_val) / (max_val-min_val)

    def get_country_list(self):
        return self.data[self.indicator].index.get_level_values('country').drop_duplicates().tolist()



import pandas as pd
import random
from comp.Airport import Airport
from comp.Route import Route

class SimulationManager:
    def __init__(self) -> None:
        self.df = self.readDataset()
        self.airports = self.AddRandomAirport(5)
        self.routes = self.AddRandomRoute(5)

    def run(self):
        pass

    def readDataset(self):
        df = pd.read_csv(r"C:\Users\alex2\Desktop\AirTrafficManager\data\airports.csv",
                         usecols=['type',
                                  'name',
                                  'latitude_deg',
                                  'longitude_deg',
                                  'elevation_ft',
                                  'iso_country',
                                  'municipality',
                                  'gps_code'])
        df = df.loc[df['type'].isin(['medium_airport', 'large_airport'])]
        df = df.dropna()
        return df

    def AddRandomAirport(self, n):
        df = self.df.sample(n, random_state=0, replace=False)
        ap = []
        for __, row in df.iterrows():
            ap.append(Airport(ICAO = row[7], city = row[6], country=row[5], lat = row[2], lon=row[3]))
        return ap

    def AddRandomRoute(self, n):
        rt = []
        for i in range(5):
            ap1, ap2 = random.sample(self.airports, 2)
            rt.append(Route(ap1.ICAO, ap2.ICAO))
        return rt


if __name__ == '__main__':
    sm = SimulationManager()
    for i in sm.airports:
        print(i)

    for i in sm.routes:
        print(i)
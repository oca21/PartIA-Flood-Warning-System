#TESTING GEO.PY#
from floodsystem.geo import stations_by_distance


class MonitoringStation:

    def __init__(self, station_id, measurement_id, name, coord, low_high_levels, river, town):
        self.station_id = station_id
        self.measurement_id = measurement_id
        self.name = name
        self.coord = coord
        self.low_high_levels = low_high_levels
        self.river = river
        self.town = town

    def __repr__(self) -> str:
        print(self.name)
        return self.name


TestStation1= MonitoringStation(
station_id='Test Station 1 station id',
measure_id='Test station 1 measure id',
label='test station 1',
coord=(0,0,1),
typical_range=(-1,3),
river='Test station 1 river',
town='Test station 1 town')

TestStation2= MonitoringStation(
station_id='Test Station 2 station id',
measure_id='Test station 2 measure id',
label='test station 2',
coord=(1,2,3),
typical_range=(-3,3),
river='Test station 2 river',
town='Test station 2 town')


stations=[TestStation1, TestStation2]


#TEST TASK 1B
#------------------------------------------------
assert stations_by_distance(stations, (0, 0))
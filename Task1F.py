import floodsystem.station as station
from floodsystem.stationdata import build_station_list
stations = build_station_list()
print(sorted(station.inconsistent_typical_range_stations(stations)))


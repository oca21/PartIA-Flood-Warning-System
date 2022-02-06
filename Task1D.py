from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list
stations = build_station_list()
print(len(rivers_with_station(stations)))
#print("The stations by River Aire are: " + str(sorted(stations_by_river(stations)['River Aire'])))
#print("The stations by River Cam are: " + str(sorted(stations_by_river(stations)['River Cam'])))
#print("The stations by River Thames are: " + str(sorted(stations_by_river(stations)['River Thames'])))
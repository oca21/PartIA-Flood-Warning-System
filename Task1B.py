from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
stations = build_station_list()

closest = []
farthest = []
sorted_stations = stations_by_distance(stations, (52.2053, 0.1218))
for i in range(len(sorted_stations)):
    if i < 10:
        closest.append((sorted_stations[i][0].name, sorted_stations[i][0].town, sorted_stations[i][1]))
    if i > len(sorted_stations) - 10:
        farthest.append((sorted_stations[i][0].name, sorted_stations[i][0].town, sorted_stations[i][1]))
print(closest)
print(farthest)
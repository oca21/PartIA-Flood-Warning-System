from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
import floodsystem.flood as flood
stations = build_station_list()
update_water_levels(stations)

listed=flood.stations_highest_rel_level(stations, 10)
for i in range(len(listed)):
    print(listed[i][0], listed[i][1])
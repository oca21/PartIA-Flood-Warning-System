from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
import floodsystem.flood as flood
stations = build_station_list()
update_water_levels(stations)
#print(station.inconsistent_typical_range_stations(stations))

stations = sorted(station.consistent_typical_range_stations(stations), key=lambda x: x.name)
stationslot=flood.stations_level_over_threshold(stations, 0.8)
for i in range(len(stationslot)):
    print(stationslot[i][0], stationslot[i][1])

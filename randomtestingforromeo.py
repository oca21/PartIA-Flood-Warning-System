from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
import floodsystem.flood as flood
stations = build_station_list()
update_water_levels(stations)

print(stations[0].typical_range[0])
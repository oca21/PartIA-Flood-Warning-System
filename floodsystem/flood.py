from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
from .utils import sorted_by_key
stations = build_station_list()
update_water_levels(stations)
stations=station.consistent_typical_range_stations(stations)

#-------------------------------------------------------------------------------------------------------#
#Task 2B
def stations_level_over_threshold(stations, tol):
    listuple=[]
    for i in range(len(stations)):
        if stations[i].relative_water_level() != None and stations[i].typical_range_consistent() != False:
            ratio=stations[i].relative_water_level()
            if ratio > tol and ratio < 20:
                listuple.append((stations[i].name, ratio))
    return sorted_by_key(listuple, 1, reverse=True)

#-------------------------------------------------------------------------------------------------------#
#Task 2C
def stations_highest_rel_level(stations, N):
    listuple = []
    outputlist = []
    for i in range(len(stations)):
        if stations[i].relative_water_level() != None and stations[i].typical_range_consistent() != False and stations[i].relative_water_level()<20:
            ratio=stations[i].relative_water_level()
            listuple.append((stations[i].name, ratio))
    sortedstations=sorted_by_key(listuple, 1, reverse=True)
    for i in range(N):
        outputlist.append((sortedstations[i][0], sortedstations[i][1]))
    return outputlist

#-------------------------------------------------------------------------------------------------------#
        
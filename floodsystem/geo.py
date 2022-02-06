"""This module contains a collection of functions related to
geographical data.
"""
from .utils import sorted_by_key  # noqa
#------------------------------------------------#
###TASK 1B###
from haversine import haversine, Unit
def stations_by_distance(stations, p):
    lists=[]
    for i in range(len(stations)):
        distance=haversine(stations[i].coord, p)
        lists.append((stations[i], distance))
    return sorted_by_key(lists, 1, reverse=False)
#------------------------------------------------#
pass
###TASK1C###
def stations_within_radius(stations, centre, r):

     # Build list of stations
    stations = build_station_list()

#------------------------------------------------# 
    for station in stations:
        if station.name in [

        ]:
            print(station)

#------------------------------------------------#
###TASK 1D###
def rivers_with_station(stations):
    rivers=[]
    for i in range(len(stations)):
        rivers.append(stations[i].river)
    return set(rivers)



def stations_by_river(stations):
    dictrivers={}
    for i in range(len(stations)):
        if stations[i].river in dictrivers:
            dictrivers[stations[i].river].append(stations[i].name)
        else:
            dictrivers[stations[i].river]=[stations[i].name]
    return dictrivers






#------------------------------------------------#
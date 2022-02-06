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


#------------------------------------------------#
###TASK 1D###
#def rivers_with_station(stations):




#------------------------------------------------#
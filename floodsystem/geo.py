"""This module contains a collection of functions related to
geographical data.
"""
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
#------------------------------------------------#
###TASK 1B###
from haversine import haversine, Unit
def stations_by_distance(stations, p):
    lists=[]
    for i in range(len(stations)): #For each station
        distance=haversine(stations[i].coord, p) #Calculate distance of the station from the coord p
        lists.append((stations[i], distance)) #Add this to list of tuples of the form (station, distance)
    return sorted_by_key(lists, 1, reverse=False) #Return the sorted list based off the distance from p
#------------------------------------------------#
###TASK1C###
def stations_within_radius(stations, centre, r):
    stations_within_r=[]

    stations_with_distance = stations_by_distance(stations, centre) #Get stations and distance from centre 
    for i in range(len(stations_with_distance)):
        if stations_with_distance[i][1]<r:
            stations_within_r.append(stations_with_distance[i][0].name)
    return stations_within_r


#------------------------------------------------#
###TASK 1D###
#def rivers_with_station(stations):




#------------------------------------------------#
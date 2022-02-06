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
    stations_within_r = []

    stations_with_distance = stations_by_distance(stations, centre) #Get stations and distance from centre 
    for i in range(len(stations_with_distance)): #For each station
        if stations_with_distance[i][1]<r: #If the distance of the station from the centre is less than the radius
            stations_within_r.append(stations_with_distance[i][0].name) #Add this station's name to the stations in the radius list
    return stations_within_r

#------------------------------------------------#
###TASK 1D###
def rivers_with_station(stations):
    rivers=[] 
    for i in range(len(stations)):
        rivers.append(stations[i].river) #Add this to total rivers list
    return set(rivers) #Return sit of the rivers list to remove duplicates



def stations_by_river(stations):
    dictrivers={}
    for i in range(len(stations)):
        if stations[i].river in dictrivers: #If the station's river is already in the dictionary
            dictrivers[stations[i].river].append(stations[i].name) #Add the station to the value relating to the river
        else:
            dictrivers[stations[i].river]=[stations[i].name] #If the river isn't in the dictionary then add the station as the value
    return dictrivers


#------------------------------------------------#
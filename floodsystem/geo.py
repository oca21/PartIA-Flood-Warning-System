"""This module contains a collection of functions related to
geographical data.
"""
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
#------------------------------------------------#
###TASK 1B###
from haversine import haversine
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
###TASK 1E###
def rivers_by_station_number(stations, N):
    numberrivers={}
    for i in range(len(stations)): #makes a dictionary with the key being the name of the river and the item being the number of stations by the river
        if stations[i].river in numberrivers:
            numberrivers[stations[i].river]+=1
        else:
            numberrivers[stations[i].river]=1 
    listrivers=(numberrivers.items()) #Converts it to a list of tuples of the form (river, number of stations by this river)
    listrivers=sorted_by_key(listrivers, i=1, reverse=True) #Sorts the list of tuples by number of river (in descending order)
    printthis=[]
    for i in range(N): #Adds the first N stations to a list to be diisplayed
        printthis.append(listrivers[i])
    for i in range(N, len(listrivers)):
        if listrivers[N-1]==listrivers[i]: #Checks if there are any other river with the same number of stations as the Nth river
            printthis.append(listrivers[i]) 
    return printthis

        
        
        
    


#------------------------------------------------#
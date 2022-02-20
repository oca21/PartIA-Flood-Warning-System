# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from operator import truediv


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

#-------------------------------------------------------------------------------------------------------#
    #TASK 1F
    def typical_range_consistent(self):
        if (self.typical_range != None): #If the data is available
            if ((self.typical_range[1] >= self.typical_range[0])): #If the high tide value is greater than or equal to the low tide value
                return True # Then the data is consistent
            else:
                return False #Else data is not consistent
        else:
            return False #Data is not consistent if not available
        
#-------------------------------------------------------------------------------------------------------#
    #TASK 2B
    def relative_water_level(self):
        if self.typical_range != None and self.latest_level != None: # If the data is available
            #and self.latest_level != None:
            current = self.latest_level - self.typical_range[0] #Find how far in between it is
            levelrange = self.typical_range[1] - self.typical_range[0] # Find the difference between the high and low
            ratio = current / levelrange # work out the ratio between the difference between the value and minimum to the max differencec
            return ratio
        else:
            return None


def inconsistent_typical_range_stations(stations):
    inconsistent_stations = []
    for i in range(len(stations)): #For each station
        if stations[i].typical_range_consistent() == False: #If the station has an inconsistent typical_range
            inconsistent_stations.append(stations[i].name) #Add this station to the inconsistent stations list ß
    return inconsistent_stations

#-------------------------------------------------------------------------------------------------------#
#testing?
def consistent_typical_range_stations(stations):
    consistent_stations = []
    for i in range(len(stations)): #For each station
        if stations[i].typical_range_consistent() != False: #If the station has an inconsistent typical_range
            consistent_stations.append(stations[i]) #Add this station to the inconsistent stations list ß
    return consistent_stations

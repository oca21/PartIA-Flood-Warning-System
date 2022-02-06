# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def hi():
    pass

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
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list

def hi():
    pass

def stations_within_radius(stations, centre, r):

     # Build list of stations
    stations = build_station_list()

    for station in stations:
        if station.name in [

        ]:
            print(station)

# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
import floodsystem.station as station

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "a"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "b"
    coord = (-2.0, 4.0)
    trange = (5.2, 3.4445)
    river = "River X"
    town = "My Town"
    b = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "c"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    c = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    range_a = MonitoringStation.typical_range_consistent(a)
    assert range_a == True
    range_b = MonitoringStation.typical_range_consistent(b)
    assert range_b == False
    range_c = MonitoringStation.typical_range_consistent(c)
    assert range_c == False

def test_inconsistent_typical_range_station():
     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "a"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "b"
    coord = (-2.0, 4.0)
    trange = (5.2, 3.4445)
    river = "River X"
    town = "My Town"
    b = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "c"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    c = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations = [a, b, c]
    station_list =(sorted(station.inconsistent_typical_range_stations(stations)))
    assert station_list == [b.name, c.name]

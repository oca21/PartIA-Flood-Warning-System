#TESTING GEO.PY#
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation

#TEST TASK 1B
#------------------------------------------------
def test_stations_by_distance():
    s_id = "testSid1"
    m_id = "testMid1"
    label = "TS1"
    coord = (1.0, 4.0)
    trange = (-2, 5)
    river = "River 1"
    town = "My Town 1"
    Test1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "testSid2"
    m_id = "testMid2"
    label = "TS2"
    coord = (0.0, 1.0)
    trange = (-2, 2)
    river = "River 2"
    town = "Town 2"
    Test2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "testSid3"
    m_id = "testMid3"
    label = "TS3"
    coord = (1.0, 1.0)
    trange = (-2, 2)
    river = "River 3"
    town = "Town 3"
    Test3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations=[Test1, Test2, Test3]
    TestResult=stations_by_distance(stations, (0, 0))
    assert (TestResult[0][0], TestResult[1][0], TestResult[2][0]) == (Test2, Test3, Test1)

#TEST RIVERS WITH STATIONS
def test_rivers_with_station():
    s_id = "testSid1"
    m_id = "testMid1"
    label = "TS1"
    coord = (1.0, 4.0)
    trange = (-2, 5)
    river = "River Thames"
    town = "My Town 1"
    Test1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "testSid2"
    m_id = "testMid2"
    label = "TS2"
    coord = (0.0, 1.0)
    trange = (-2, 2)
    river = "River Thames"
    town = "Town 2"
    Test2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "testSid3"
    m_id = "testMid3"
    label = "TS3"
    coord = (1.0, 1.0)
    trange = (-2, 2)
    river = "River 3"
    town = "Town 3"
    Test3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)


#rivers_with_station, stations_by_river

#Test Task1C#------------------------------

def test_stations_within_radius():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "a"
    coord = (-0.1, 0.03)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "b"
    coord = (0.1, 0.12)
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
    stations_near_origin = sorted(stations_within_radius(stations, (0,0), 18))  
    assert stations_near_origin == [a.name, b.name]  

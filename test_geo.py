#TESTING GEO.PY#
from floodsystem.geo import stations_by_distance
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
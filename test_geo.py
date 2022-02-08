#TESTING GEO.PY#
from floodsystem.geo import stations_by_distance, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation

#Test Task 1B
#-----------------------------------------------------
#Test haversine function
def test_haversine():
    from haversine import haversine, Unit
    Coord1=(0.0,0.0)
    Coord2=(0.1,7.0)
    Coord3=(1.0,2.0)
    assert haversine(Coord1, Coord1)==0
    assert round(haversine(Coord2, Coord1), 1)==778.4
    assert round(haversine(Coord3, Coord1),1)==248.6

#test stations_by_distance
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

#Test Task 1D
#-----------------------------------------------------
#test stations_by_river
def test_stations_by_river():
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

    stations=[Test1, Test2, Test3]

    assert sorted(stations_by_river(stations)['River Thames']) == [Test1.name, Test2.name]

#test rivers_with_stations
def test_rivers_with_stations():
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

    stations=[Test1, Test2, Test3]


    assert rivers_with_station(stations) == {'River 3', 'River Thames'}

#Test1C

#Test Task 1E
#-----------------------------------------------------
def test_rivers_by_station_number():
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

    stations=[Test1, Test2, Test3]

    assert rivers_by_station_number(stations,2)[0][0] == "River Thames"
    assert rivers_by_station_number(stations,2)[0][1] == 2
    assert rivers_by_station_number(stations,2)[1][0] == "River 3"
    assert rivers_by_station_number(stations,2)[1][1] == 1
test_rivers_by_station_number()
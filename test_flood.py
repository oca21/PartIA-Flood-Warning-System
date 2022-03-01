from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
#-------------------------------------------------------------------------------------------------------#
#Task 2B
def test_relative_water_level(self):
    if self.label=="TS1":
        return 0.1
    elif self.label=="TS2":
        return 0.5
    elif self.label=="TS3":
        return 1


def test_stations_level_over_threshold():
    s_id = "testSid1"
    m_id = "testMid1"
    label = "TS1"
    coord = (1.0, 4.0)
    trange = (0, 5)
    river = "River 1"
    town = "My Town 1"
    latest_level=10
    Test1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "testSid2"
    m_id = "testMid2"
    label = "TS2"
    coord = (0.0, 1.0)
    trange = (-2, 2)
    river = "River 2"
    town = "Town 2"
    latest_level=0.2
    Test2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "testSid3"
    m_id = "testMid3"
    label = "TS3"
    coord = (1.0, 1.0)
    trange = (-2, 2)
    river = "River 3"
    town = "Town 3"
    latest_level=0
    Test3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)


    stations=[Test1, Test2, Test3]
    print(stations_level_over_threshold(stations, 0.8))
    #assert(stations_level_over_threshold(stations, 0.8))==
test_stations_level_over_threshold()

#-------------------------------------------------------------------------------------------------------#
#Task 2C
#def test_stations_highest_rel_level():
#    listuple = []
#    outputlist = []
#    for i in range(len(stations)):
#        if stations[i].relative_water_level() != None and stations[i].typical_range_consistent() != False and stations[i].relative_water_level()<20:
#            ratio=stations[i].relative_water_level()
#            listuple.append((stations[i].name, ratio))
#    sortedstations=sorted_by_key(listuple, 1, reverse=True)
#    for i in range(N):
#        outputlist.append((sortedstations[i][0], sortedstations[i][1]))
#    return outputlist

#-------------------------------------------------------------------------------------------------------#
        
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
#import floodsystem.station as station

stations = build_station_list()
update_water_levels(stations)
stations_and_rel_level = stations_highest_rel_level(stations, 5)
for i in range(5):
    for station in stations:
        for index, tuple in enumerate(stations_and_rel_level):
            station_at_risk = None

            for station in stations:
                if station.name == tuple[0]:
                    station_at_risk = station
                    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
                    if dates:
                        plot_water_level_with_fit(station, dates, levels, 4)
                    else:
                        print("Could not fetch measure levels for", station.name)


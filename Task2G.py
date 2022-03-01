# rank all stations based on risk level

import re
import matplotlib.dates
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import predict_future_level
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()
update_water_levels(stations)

def station_risk_level(station):
    level_today = 1
    """
    try:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=4))
        level_tommorow = predict_future_level(dates, levels)[1]
        level_today = station.relative_water_level() or 1
        relative_level_tomorrow = (level_tommorow - level_today /level_today)
    except:
        print("Something happened")
        relative_level_tomorrow = 1
    """
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=4))
    level_tommorow = predict_future_level(dates, levels)[1]
    level_today = station.relative_water_level() or 1
    relative_level_tomorrow = (level_tommorow - level_today /level_today)
    #print("Level today is " + str(level_today))
    #print("Relative level tomorrow is " + str(relative_level_tomorrow))
    #print("Level tomorrow is " + str(level_tommorow))
    if level_today > 2 or relative_level_tomorrow > 2:
        return "Severe"
    elif level_today >1.7 or relative_level_tomorrow >1.7:
        return "High"
    elif level_today >1.3 or relative_level_tomorrow >1.3:
        return "Moderate"
    else:
        return "Low"

for station in stations:
    try:
        print("Risk Level for", station.name, "is", station_risk_level(station))
    except:
        print("Risk level for", station.name, "is unavailable")
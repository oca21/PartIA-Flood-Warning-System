from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
#from floodsystem.flood import stations_highest_rel_level
#from floodsystem.analysis import polyfit
#from floodsystem.plot import plot_water_level_with_fit
stations = build_station_list()
dt=10
# for Task 2F

def polyfit(dates, levels, p):

    dates_shifted = []
    d0 = dates[-1]

    for date in dates:
        dates_shifted.append(date - d0)

    p_coeff = np.polyfit(dates_shifted, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0


dates, levels = fetch_measure_levels(
        stations[0].measure_id, dt=datetime.timedelta(days=dt))
print(dates)
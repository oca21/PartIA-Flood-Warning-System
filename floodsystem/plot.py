from datetime import date
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels, label=station.name)
    lows=np.zeros(len(dates))
    highs=np.zeros(len(dates))
    for i in range(len(dates)):
        lows[i]=station.typical_range[0]
        highs[i]=station.typical_range[1]
    plt.plot(dates, lows, label="typical low")
    plt.plot(dates, highs, label="typical high")
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    #plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):

    low = []
    high = []
    for i in range(30):
        low.append(station.typical_range[0])
        high.append(station.typical_range[1])
        i += 1
    
    poly, d0 = polyfit(dates, levels, p)
    dates_shifted = []
    dates_float = matplotlib.dates.date2num(dates)

    for i in range(len(dates_float)):
        dates_shifted.append(dates_float[i] - d0)

    plt.plot(dates_shifted, levels, '.', label = "fetched data")

    x1 = np.linspace(dates_shifted[0], dates_shifted[-1], 30)
    plt.plot(x1, poly(x1), label = "polynomial best fit")

    plt.plot(x1, high, 'r--', label = "typical range")
    plt.plot(x1, low, 'r--')

    plt.ylabel("water level for {}".format(station.name))
    plt.xlabel("days passed")
    plt.legend()

    plt.show()

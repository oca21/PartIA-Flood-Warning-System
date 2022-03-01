import matplotlib.pyplot as plt
import numpy as np

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
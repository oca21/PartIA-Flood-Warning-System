from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood
import floodsystem.plot as plot
from datetime import datetime, timedelta
stations = build_station_list()
update_water_levels(stations)

import datetime
from floodsystem.datafetcher import fetch_measure_levels

listed=flood.stations_highest_rel_level(stations, 5)

for i in range(5):
     station_name = listed[i][0]
     # Find station
     station_ = None
     for station in stations:
          if station.name == station_name:
               station_ = station
               break

     if not station_:
          print("Station {} could not be found".format(station_name))

     dt = 10
     dates, levels = fetch_measure_levels(station_.measure_id, dt=datetime.timedelta(days=dt))

     plot.plot_water_levels(station, dates, levels)

     # Plot
     ##plt.plot(dates, levels, label=station_.name)

     # Add axis labels, rotate date labels and add plot title
     ##plt.xlabel('date')
     ##plt.ylabel('water level (m)')
     ##plt.xticks(rotation=45);
     ##plt.title("Stations")
     ##plt.title("Station {}".format(i))


##plt.tight_layout()  # This makes sure plot does not cut off date labels
##plt.legend()
##plt.show()
#double hashtag uncomment these to have all graphs in one 
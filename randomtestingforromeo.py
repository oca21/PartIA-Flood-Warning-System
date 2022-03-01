stations = build_station_list()
update_water_levels(stations)
stations_and_rel_level = stations_highest_rel_level(stations, 5)
for i in range(5):
    print("loop1")
    for station in stations:
        print("loop2")
        for index, tuple in enumerate(stations_and_rel_level):
            station_at_risk = None
            print("loop3")
            for station in stations:
                print("loop4")
                if station.name == tuple[0]:
                    station_at_risk = station
                    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
                    print("loop5")
                    if dates:
                        plot_water_level_with_fit(station, dates, levels, 4)
                    else:
                        print("Could not fetch measure levels for", station.name)
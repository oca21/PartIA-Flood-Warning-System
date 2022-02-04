from mimetypes import init


class MonitoringStation:

    def __init__(self, station_id, measurement_id, name, coord, low_high_levels, river, town):
        self.station_id = station_id
        self.measurement_id = measurement_id
        self.name = name
        self.coord = coord
        self.low_high_levels = low_high_levels
        self.river = river
        self.town = town

    def __repr__(self) -> str:
        print(self.name)
        return self.name


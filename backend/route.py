from connector import cur


class Route:
    def __init__(self, id, station_id, station_name):
        self.routId = id
        self.stationId = station_id
        self.stationName = station_name

    def add(self):
        # save to db
        pass

    def delete(self):
        # delete from db
        pass



from backend.connector import cur, client


class Route:
    def __init__(self, id, station_id, station_name, start, end):
        self.routId = id
        self.stationId = station_id
        self.stationName = station_name
        self.start = start
        self.end = end

    def add(self):
        values= (self.routId, self.stationId, self.stationName, self.start, self.end)
        cur.execute('insert into new_route values(?, ?, ?, ?, ?)', values)
        client.commit()

    def delete(self):
        # delete from db
        pass



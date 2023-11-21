from backend.connector import cur, client


class Route:
    def __init__(self, id, station_id, station_name):
        self.routId = id
        self.stationId = station_id
        self.stationName = station_name

    def add(self):
        values= (self.routId, self.stationId, self.stationName)
        cur.execute('insert into new_route values(?, ?, ?)', values)
        client.commit()

    def delete(self):
        # delete from db
        pass



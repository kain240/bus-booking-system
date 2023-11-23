from backend.connector import cur, client


class Route:
    def __init__(self, id, start, stop):
        self.routId = id
        self.start = start
        self.stop = stop

    def get_values(self):
        return (self.routId, self.start, self.stop)
    def add(self):
        values = self.get_values()
        cur.execute('insert into route values(?, ?, ?)', values)
        client.commit()

    def delete(self):
        cur.execute('delete from route where id=?', (self.routId,))
        client.commit()



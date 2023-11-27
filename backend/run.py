import uuid

from backend.connector import cur, client


class Run:
    def __init__(self, bus_id, route_id, running_date, seat_available):
        self.id = uuid.uuid4().hex
        self.busId = bus_id
        self.runningDate = running_date
        self.available = seat_available
        self.routeId = route_id

    def add(self):
        values = (self.id, self.busId, self.routeId, self.runningDate, self.available)
        cur.execute('insert into run values(?, ?, ?, ?, ?)', values)
        client.commit()

    def delete(self):
        values = (self.busId, self.routeId, self.runningDate)
        cur.execute('select id from run where bus_id= ? and route_id=? and running_date= ? ', values)
        ids = cur.fetchall()

        if ids:
            # Extracting the ID properly
            id_to_delete = ids[0][0]  # Assuming you want to delete the first ID from the result

            # Deleting using the extracted ID
            cur.execute('DELETE FROM run WHERE id=?', (id_to_delete,))
            client.commit()
        else:
            print("No matching entry found.")


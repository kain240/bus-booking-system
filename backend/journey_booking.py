import uuid
from backend.connector import cur, client


class Booking:
    run_id: int
    payment: bool

    def __init__(self, start, end, date):
        self.id = uuid.uuid4()
        self.start = start
        self.end = end
        self.date = date

    def find_runs(self):

        print(f"finding runs(operator, bus_type, fare, seats_available) for trip({self.start} to {self.end} on {self.date})")
        result = []
        # fetching all the route_ids(routes) where start and stop the search input
        cur.execute('SELECT id FROM route WHERE start = ? AND stop = ?', (self.start, self.end))
        route_ids = tuple([row[0] for row in cur.fetchall()])
        placeholders = ','.join(['?'] * len(route_ids))

        # fetching all runs where running_date and route_ids match to get bus_info
        cur.execute(f'SELECT bus_id, available FROM run WHERE running_date = ? AND "route_id" IN ({placeholders})',
                    ((self.date,) + route_ids))
        trips = cur.fetchall()

        for trip in trips:
            cur.execute(f'SELECT operator_id, type, fare FROM bus WHERE id = ? ', (trip[0],))
            bus_info = cur.fetchall()

            for bus in bus_info:

                cur.execute('SELECT name FROM operator WHERE id = ? ', (bus[0],))
                operator = cur.fetchall()

                operator_name = operator[0][0]
                bus_type = bus[1]
                fare = bus[2]
                seats_available = trip[1]

                result.append((operator_name, bus_type, seats_available, fare))

        return result


def get_booking():
    all_bookings = cur.execute('select * from journey_booking, where passenger_id = passenger_id')
    return all_bookings


class Booking2:
    run_id: int
    payment: bool

    def __init__(self, passenger_id, run_id):
        self.id = uuid.uuid4().hex
        self.passenger_id = passenger_id
        self.run_id = run_id

    def set_booking(self):
        values = (self.id, self.passenger_id, self.run_id)
        cur.execute('insert into booking values(?, ?, ?)', values)
        client.commit()

    def update_booking(self):
        cur.execute('update booking set passenger_id = ?, run_id = ? where id = ?', (self.passenger_id, self.run_id, self.id))
        client.commit()

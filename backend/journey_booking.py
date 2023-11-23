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
        cur.execute('SELECT id FROM route WHERE start = ? AND stop = ?', (self.start, self.end))
        route_ids = tuple([row[0] for row in cur.fetchall()])
        placeholders = ','.join(['?'] * len(route_ids))

        cur.execute(f'SELECT bus_id, available FROM run WHERE running_date = ? AND "route_id" IN ({placeholders})', ((self.date,) + route_ids))
        trip1 = cur.fetchall()

        cur.execute('SELECT id FROM bus WHERE id = ? ',(trip1[0][0],))
        route_ids2 = tuple([row[0] for row in cur.fetchall()])
        placeholders2 = ','.join(['?'] * len(route_ids2))

        cur.execute(f'SELECT type, fare, operator_id FROM bus WHERE id IN ({placeholders2})', route_ids2)
        trip2 = cur.fetchall()

        cur.execute('SELECT id FROM operator WHERE id = ? ', (trip2[0][2],))
        route_ids3 = tuple([row[0] for row in cur.fetchall()])
        placeholders3 = ','.join(['?'] * len(route_ids3))

        cur.execute(f'SELECT name FROM operator WHERE id IN ({placeholders3})', route_ids3)
        trip3 = cur.fetchall()

        # Combine the results
        trips = trip3 + trip2 + trip1
        print(trips)
        return trips


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

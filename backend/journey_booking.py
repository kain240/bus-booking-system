import uuid
from backend.connector import cur, client


class Booking:

    def __init__(self, start, end, date):
        self.id = uuid.uuid4()
        self.start = start
        self.end = end
        self.date = date

    def find_runs(self):

        print(
            f"finding runs(operator, bus_type, fare, seats_available) for trip({self.start} to {self.end} on {self.date})")
        result = []
        # fetching all the route_ids(routes) where start and stop the search input
        cur.execute('SELECT id FROM route WHERE start = ? AND stop = ?', (self.start, self.end))
        route_ids = tuple([row[0] for row in cur.fetchall()])
        placeholders = ','.join(['?'] * len(route_ids))

        # fetching all runs where running_date and route_ids match to get bus_info
        cur.execute(f'SELECT id, bus_id, available FROM run WHERE running_date = ? AND "route_id" IN ({placeholders})',
                    ((self.date,) + route_ids))
        trips = cur.fetchall()

        for trip in trips:
            cur.execute(f'SELECT operator_id, type, fare FROM bus WHERE id = ? ', (trip[1],))
            bus_info = cur.fetchall()

            for bus in bus_info:
                cur.execute('SELECT name FROM operator WHERE id = ? ', (bus[0],))
                operator = cur.fetchall()

                trip_id = trip[0]
                operator_name = operator[0][0]
                bus_type = bus[1]
                fare = bus[2]
                seats_available = trip[2]

                result.append((trip_id, operator_name, bus_type, seats_available, fare))

        return result


# def get_booking():
#     all_bookings = cur.execute('select * from journey_booking, where passenger_id = passenger_id')
#     return all_bookings


class BookingTicket:
    def __init__(self, passenger_id, run_id):
        self.id = uuid.uuid4().hex
        self.passenger_id = passenger_id
        self.run_id = run_id

    def set_booking(self):
        values = (self.id, self.passenger_id, self.run_id)
        cur.execute('insert into booking values(?, ?, ?)', values)
        client.commit()


def get_booking(passenger_mobile_num):
    cur.execute('select run_id from booking where passenger_id = ?', (passenger_mobile_num,))
    run_ids = tuple([row[0] for row in cur.fetchall()])

    placeholders = ','.join(['?' for _ in run_ids])
    query = f'SELECT name, gender, no_seats, mobile_num, age, run_id FROM passenger WHERE mobile_num = ? AND "run_id" IN ({placeholders})'
    parameters = (passenger_mobile_num,) + tuple(run_ids)
    cur.execute(query, parameters)
    tickets = cur.fetchall()
    return tickets

def get_running_date(ID):
    cur.execute('select bus_id, route_id, running_date from run where id= ?', (ID,))
    ticket_date = cur.fetchall()
    print (ticket_date)
    return ticket_date[0]

def get_to_from(ID):
    cur.execute('select start, stop from route where id= ?', (ID,))
    to_and_from = cur.fetchall()
    print (to_and_from)
    return to_and_from[0]

def get_fare_type(ID):
    cur.execute('select fare, type, operator_id from bus where id= ?', (ID,))
    fare_and_type= cur.fetchall()
    return fare_and_type[0]

def get_bus_name(ID):
    cur.execute('select name from operator where id= ?', (ID,))
    bus_name= cur.fetchall()
    return bus_name[0][0]








# fare, bus, type
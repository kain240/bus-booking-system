from backend.connector import cur, client


class Booking:
    def __init__(self, start, end, date):
        self.start = start
        self.end = end
        self.date = date

    def find_runs(self):
        pass
        # routes = cur.execute('select id from new_route where new_route."from"= self.start & new_route.end = self.end')
        # trips = {trip.date = self.date and trip.route_id $in routes }
        # return trips


    def show_run(self):
        # find_runs()
        pass


    def make_booking(self):
        values = (self.start, self.end, self.date)
        cur.execute('INSERT INTO journey_booking ("to", "from", "date") VALUES (?, ?, ?)', values)
        client.commit()

    def update_booking(self):
        # booking
        pass

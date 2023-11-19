# import run
# import passenger
from backend.connector import cur


class Booking:
    def __init__(self, start, end, date):
        self.start = start
        self.end = end
        self.date = date

    def find_runs(self,date,start,end):
        # run_coll.find()
        pass

    def show_run(self):
        # run
        pass

    def make_booking(self):
        cur.execute('insert into journey_booking values(self.start, self.end, self.date)')
        cur.execute('select * from journey_booking')

    def update_booking(self):
        # booking
        pass

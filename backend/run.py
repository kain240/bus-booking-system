from connector import cur


class Run:
    def __init__(self, bus_id, running_date, seat_available):
        self.busId = bus_id
        self.runningDate = running_date
        self.available = seat_available

    def add(self):
        # save to db
        pass

    def delete(self):
        # delete from db
        pass
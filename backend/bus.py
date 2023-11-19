from connector import cur


class Bus:
    def __init__(self, bus_id, bus_type, capacity, fare, operator_id, route_id):
        self.busId = bus_id
        self.busType = bus_type
        self.capacity = capacity
        self.fare = fare
        self.operatorId = operator_id
        self.routeId = route_id

    def add(self):
        # save to db
        pass

    def edit(self):
        # alter in db
        pass

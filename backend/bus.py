from backend.connector import cur, client


class Bus:
    def __init__(self, bus_id, bus_type, capacity, fare, operator_id, route_id):
        self.busId = bus_id
        self.busType = bus_type
        self.capacity = capacity
        self.fare = fare
        self.operatorId = operator_id
        self.routeId = route_id

    def add(self):
        values = (self.busId, self.busType, self.capacity, self.fare, self.operatorId, self.routeId)
        cur.execute('insert into new_bus ("bus_id" , "bus_type" , "capacity" , "fare" , "operator_id" , "route_id") values(?, ?, ?, ?, ?, ?)', values)
        client.commit()

    def edit(self):
        # alter in db
        pass

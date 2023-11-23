from backend.connector import cur, client


class Bus:
    def __init__(self, bus_id, bus_type, capacity, fare, operator_id):
        self.busId = bus_id
        self.busType = bus_type
        self.capacity = capacity
        self.fare = fare
        self.operatorId = operator_id

    def get_values(self):
        return (self.busId, self.busType, self.capacity, self.fare, self.operatorId)

    def add(self):
        values = self.get_values()
        cur.execute('insert into bus values(?, ?, ?, ?, ?)', values)
        client.commit()

    def edit(self):
        values = self.get_values()
        cur.execute('update bus set id=?, type=?, capacity=?, fare=?, operator_id=? where id = ?', values + (self.busId,))
        client.commit()

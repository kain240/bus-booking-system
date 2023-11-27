from backend.connector import cur, client


class Operator:
    def __init__(self, operator_id, name, address, phone, email):
        self.operatorId = operator_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def add(self):
        values = (self.operatorId, self.name, self.address, self.phone, self.email)
        cur.execute('INSERT INTO operator VALUES (?, ?, ?, ?, ?)', values)
        client.commit()
    def edit(self):
        values = (self.operatorId, self.name, self.address, self.phone, self.email)
        cur.execute('update operator set id=?, name=?, address=?, phone=?, email=? where id=?', (values, self.operatorId))
        client.commit()



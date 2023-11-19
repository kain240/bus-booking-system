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
        cur.execute('INSERT INTO new_operator ("operator_id", "operator_name", "operator_address", "operator_phone", "operator_email") VALUES (?, ?, ?, ?, ?)', values)
        client.commit()
    def edit(self):
        # alter in db
        pass




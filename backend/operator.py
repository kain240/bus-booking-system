from connector import cur


class Operator:
    def __init__(self, operator_id, name, address, phone, email):
        self.operatorId = operator_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def add(self):
        # save to db
        pass
    def edit(self):
        # alter in db
        pass




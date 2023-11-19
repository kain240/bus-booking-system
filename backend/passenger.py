from connector import cur, client


class Passenger:
    def __init__(self, name, age, gender, mobile_no, no_of_seats):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobileNo = mobile_no
        self.noOfSeats = no_of_seats

    def add(self):
        values=(self.name, self.age, self.gender, self.mobileNo, self.noOfSeats)
        cur.execute('insert into passenger values(?, ?, ?, ?, ?), values')
        client.commit()
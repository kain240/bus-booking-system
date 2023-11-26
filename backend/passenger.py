import uuid

from backend.connector import cur, client
class Passenger:
    def __init__(self, name, age, gender, mobile_no, no_of_seats, run_id):
        self.name = name
        self.gender = gender
        self.noOfSeats = no_of_seats
        self.mobileNo = mobile_no
        self.age = age
        self.run_id = run_id

    def add(self):
        values =(self.name, self.gender, self.noOfSeats, self.mobileNo, self.age, self.run_id)
        cur.execute('insert into passenger("name", "gender", "no_seats", "mobile_num", "age", "run_id") values(?, ?, ?, ?, ?, ?)', values)
        client.commit()


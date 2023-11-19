from connector import cur


class Passenger:
    def __init__(self, name, age, gender, mobile_no, no_of_seats):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobileNo = mobile_no
        self.noOfSeats = no_of_seats


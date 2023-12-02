# A Bus Booking System

Where Bus services can,
* register their new operator(Operator Id, Operator name, Address, Phone, Email)
  here Operator Id, Operator name and Phone are mandatory fields.
* add their new Buses(Bus Id, type, capacity, Fare, Operator Id)
  here all the fields are mandatory.
  Operator Id must be same as filled while registering the Operator.
* set new Route(Route Id, start, stop), and
  here all the fields are mandatory.
* schedule new Run(Bus Id, Running Date, seats Available, Route Id)
  here all the fields are mandatory.
  Bus Id must be same as filled while registering the Bus.
  Route Id must be same as filled while registering the Route.

And users can,
* search for trips/buses : (to, from, date)
* by clicking on show bus it gives out the list of all the buses
* select one of the listed buses
* if there is no bus found for particular trip it will show error message: no buses found!
* enter booking details of passenger(name, gender, no. of seats, mobile number, age) and confirm booking
  here name, no. of seats and mobile number are mandatory fields.
  if any of these fields remains empty it will show error messages.
  if required no. of seats is greater than available seats it will deliver a message: seats not available
  if phone number is not of length 10 it will deliver a message: invalid mobile number
* now click on book seat, it will pop up a total amount confirmation message box
* after confirmation of amount it will show you your ticket.

* search for their tickets : using their registered mobile number
* if multiple tickets are registered with same mobile number you can view all tickets using next arrow (>)
* if no trip is registered with this mobile number it will show error
---
#### To run the app
`python3 app.py`

---
#### Sample details that are needed to be filled

new Operator -> 23456 , Kamla Travels, Guna, 1234567890, kamla@gmail.com

new Bus -> 3344, AC 3x2, 50, 550, 23456

new Route -> 9876, guna, indore

new Run -> 3344, 03-12-2023, 40, 789

* while booking
  To : indore
  From : guna
  Date : 03-12-2023


  
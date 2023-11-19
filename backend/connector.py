import sqlite3

client = sqlite3.connect('bus_db')
cur = client.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS journey_booking("to" varchar(50), "from" varchar(50), "date" DATE)')

cur.execute('CREATE TABLE IF NOT EXISTS passenger("name" varchar(30), "gender" char(1), "no_seat" int, "mobile_num" varchar(10), "age" int)')

cur.execute('CREATE TABLE IF NOT EXISTS bus_details("bus_id" varchar(10), "bus_type" varchar(6), "available" int, "fare" int, "to" varchar(50), "from" varchar(50), "running_date" DATE)')

cur.execute('CREATE TABLE IF NOT EXISTS new_operator("operator_id" varchar(10), "operator_name" varchar(30), "operator_address" varchar(50), "operator_phone" varchar(10), "operator_email" varchar(30))')

cur.execute('CREATE TABLE IF NOT EXISTS new_bus("bus_id" varchar(10), "bus_type" varchar(6), "capacity" int, "fare" int, "operator_id" varchar(10), "route_id" varchar(10))')

cur.execute('CREATE TABLE IF NOT EXISTS new_route("route_id" varchar(10), "station_id" varchar(10), "station_name" varchar(30))')

cur.execute('CREATE TABLE IF NOT EXISTS new_run("bus_id" varchar(10), "running_date" DATE, "available" int, "to" varchar(50), "from" varchar(50))')

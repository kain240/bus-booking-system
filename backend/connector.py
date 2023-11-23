import sqlite3

client = sqlite3.connect('bus_db')
cur = client.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS operator("operator_id" varchar(10), "operator_name" varchar(30), "operator_address" varchar(50), "operator_phone" varchar(10), "operator_email" varchar(30))')
cur.execute('CREATE TABLE IF NOT EXISTS bus("bus_id" varchar(10), "bus_type" varchar(6), "capacity" int, "fare" int, "operator_id" varchar(10), "route_id" varchar(10))')
cur.execute('CREATE TABLE IF NOT EXISTS route("id" varchar(10), "station_id" varchar(10), "station_name" varchar(30), "to" varchar(50), "from" varchar(50))')
cur.execute('CREATE TABLE IF NOT EXISTS run(id "bus_id" varchar(10), "running_date" DATE, "available" int)')
cur.execute('CREATE TABLE IF NOT EXISTS passenger("name" varchar(30), "gender" char(1), "no_seat" int, "mobile_num" varchar(10), "age" int)')
cur.execute('CREATE TABLE IF NOT EXISTS journey_booking("to" varchar(50), "from" varchar(50), "date" DATE)')

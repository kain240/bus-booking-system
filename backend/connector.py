import sqlite3

client = sqlite3.connect('bus_db')
cur = client.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS operator ("id" varchar(10), "name" varchar(30), "address" varchar(50), "phone" varchar(10), "email" varchar(30))')
cur.execute('CREATE TABLE IF NOT EXISTS bus      ("id" varchar(10), "type" varchar(6), "capacity" int, "fare" int, "operator_id" varchar(10))')
cur.execute('CREATE TABLE IF NOT EXISTS route    ("id" varchar(10), "start" varchar(50), "stop" varchar(50))')
cur.execute('CREATE TABLE IF NOT EXISTS run      ("id" varchar(32), "bus_id" varchar(10), "route_id" varchar(10), "running_date" DATE, "available" int)')
cur.execute('CREATE TABLE IF NOT EXISTS passenger("name" varchar(30), "gender" char(1), "no_seats" int, "mobile_num" varchar(10), "age" int)')
cur.execute('CREATE TABLE IF NOT EXISTS booking  ("id" varchar(10), "passenger_id" varchar(10), "run_id" varchar(10))')

import sqlite3, time, datetime, random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from dateutil import parser
import time
import math

style.use('fivethirtyeight')

with sqlite3.connect("discord0.db") as conn:
    c = conn.cursor()


def create_table():
    c.execute(
        '''CREATE TABLE IF NOT EXISTS plotthis(unix REAL, datestamp TEXT, usersjoined INTEGER, discordpop INTEGER)''')
    c.execute('SELECT * FROM plotthis ORDER BY discordpop DESC LIMIT 1;')
    oldpop = c.fetchall()
    if len(oldpop) and len(oldpop[0]):
        return
    unix = int(time.time())
    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    usersjoined = random.randint(-1, 3)
    discordpop = 0
    if discordpop <= 1:
        dicordpop = 0

    c.execute("INSERT INTO plotthis(unix, datestamp, usersjoined, discordpop) VALUES (?, ?, ?, ?)",
              (unix, datestamp, usersjoined, discordpop))


def dynamic_data_entry():
    c.execute('SELECT * FROM plotthis ORDER BY discordpop DESC LIMIT 1;')
    oldpop = c.fetchall()

    unix = int(time.time())
    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    usersjoined = random.randint(-4, 5)
    discordpop = oldpop[0][-1] + usersjoined

    c.execute("INSERT INTO plotthis(unix, datestamp, usersjoined, discordpop) VALUES (?, ?, ?, ?)",
              (unix, datestamp, usersjoined, discordpop))

    conn.commit()


def read_from_db():
    c.execute('SELECT discordpop FROM plotthis')
    data = c.fetchall()


def graph_data():
    c.execute('SELECT datestamp, discordpop FROM plotthis')
    data = c.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


create_table()


def timer():
    start = time.time()
    time.clock()
    elapsed = time.time() - start



def get_number():
    var = input('How many minutes you desire to simulate?\nEnter the number 10 or lower here: ')
    try:
        var = int(var)
    except ValueError:
        return get_number()
    if var > 10 or var < 0:
        return get_number()
    return var


user_input = get_number()
elapsed_time = 0
j = 0
intervals = 0
record = []

while True:
    sleep_secs = random.uniform(3, 12)
    elapsed_time += sleep_secs

    if j == 0:
        print('Simulation is running. \nIt will run for about ' + str(user_input) +  ' minute.\n')
        j = 1

    time.sleep(sleep_secs)
    dynamic_data_entry()

    intervals = (math.floor(elapsed_time) - math.floor(elapsed_time)%30)
    record.append(intervals)
    print(record)


    intervals += 1

    if elapsed_time >= user_input*60:
        break








read_from_db()

graph_data()

c.close
conn.close()

print("Complete")

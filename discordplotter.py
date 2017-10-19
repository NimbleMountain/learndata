import sqlite3, time, datetime, random
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from matplotlib import style
from dateutil import parser
    
style.use('fivethirtyeight')


with sqlite3.connect("discord0.db") as conn:

    c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS plotthis(unix REAL, datestamp TEXT, usersjoined INTEGER, discordpop INTEGER)''')
    unix = int(time.time())
    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    usersjoined = random.randint(-1,3)
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
    usersjoined = random.randint(-1,3)
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
        
    plt.plot_date(dates,values,'-')
    plt.show()
    
    
create_table()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

read_from_db()

graph_data()

c.close
conn.close()

print("Complete")


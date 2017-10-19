import sqlite3, time, datetime, random
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from matplotlib import style
from dateutil import parser
    
style.use('fivethirtyeight')

with sqlite3.connect("discord0.db") as conn:

    c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS plotthis(unix REAL, datestamp TEXT, discordpop INTEGER)''')
    

def dynamic_data_entry():
      
    unix = int(time.time())
    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    discordpop = random.randint(-1,3)
    
    c.execute("INSERT INTO plotthis(unix, datestamp, discordpop) VALUES (?, ?, ?)",
          (unix, datestamp, discordpop))

    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM plotthis')
    data = c.fetchall()
    for row in data:
        print(row)

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


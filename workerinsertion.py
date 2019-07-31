import sqlite3
import random
def insertTask(ix,name, des):



    print("worker.py created")

    conn = sqlite3.connect('home.db')
    c =  conn.cursor()

    
    c.execute('insert into Workers (WorkerID, Workername, WorkerDescription) values (?,?,?)', (int(ix),name,des))
    conn.commit()

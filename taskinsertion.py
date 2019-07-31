import sqlite3
import random
def insertTask(ix,name, des):



    print("task.py created")

    conn = sqlite3.connect('home.db')
    c =  conn.cursor()

    
    c.execute('insert into Tasks (TaskID, name, description) values (?,?,?)', (int(ix),name,des))
    conn.commit()
    conn.close()
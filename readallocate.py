import sqlite3
import random 


def readallocate(workername, taskname, assetname, timeallocate, timeperformed):

    conn = sqlite3.connect('home.db')

    c = conn.cursor()

    i = random.randint(1, 5656)

    List = []


    c.execute('SELECT * FROM Workers WHERE WorkerName = ?', (workername, ))
    for i in c:
        List.append(i[0])   
    c.execute('SELECT * FROM Tasks WHERE name = ?', (taskname, ))
    for i in c:
        List.append(i[0])

    c.execute('SELECT * FROM Assets WHERE AssetName = ?', (assetname, ))
    for i in c:
        List.append(i[0])

    TaskID = List[1]
   
    WorkerID = List[0]
    AssetID = List[2]

    c.execute('''INSERT  INTO AllocateTask (AssetID, TaskID, WokerID, TIMEALLOCATE, TIMEPERFORMED) VALUES (?,?,?,?,?)''', (TaskID, WorkerID, AssetID, timeallocate, timeperformed))

    

    conn.commit()
    
    conn.close()
    print("Done")


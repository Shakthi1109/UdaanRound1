import sqlite3

def readAssets(WorkerID):

    print("assets.py created")

    conn = sqlite3.connect('home.db')
    c =  conn.cursor()



    c.execute('SELECT * FROM AllocateTask WHERE WokerID = ?', (WorkerID, ))

    Dict = {}
    i = 0 
    for row in c:
        Dict['AssetID'] = row[0]
        Dict['TaskID']=row[1]
        Dict['WorkerID']=row[2]
        Dict['TINEALLOCATE']=row[3]
        Dict['TIMEPERFORMED']=row[4]
    return Dict

import sqlite3
import random
def insertTask(ix,name, des):



    print("assets.py created")

    conn = sqlite3.connect('home.db')
    c =  conn.cursor()

    
    c.execute('insert into Assets (AssetID, Assetname, AssetDescription) values (?,?,?)', (int(ix),name,des))
    conn.commit()

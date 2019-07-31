import sqlite3
def readAssets():
    conn = sqlite3.connect('home.db')
    c =  conn.cursor()
    c.execute('SELECT * FROM Assets')

    Dict = {}
    l=[]
    for row in c:
        Dict["name"] = row[1]
        Dict["decription"]=row[2]
        Dict={}
        l.append(Dict)
    return l

import sqlite3

def create():
	conn = sqlite3.connect('home.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE if not exists Assets ( AssetID INT NOT NULL,AssetName TEXT NOT NULL,AssetDescription TEXT NOT NULL);""")
	c.execute("""CREATE TABLE if not exists Tasks ( TaskID INT NOT NULL,name TEXT NOT NULL,description TEXT NOT NULL);""")
	c.execute("""CREATE TABLE if not exists AllocateTask ( AssetID INT NOT NULL,TaskId INT NOT NULL,WokerId INT NOT NULL, TIMEALLOCATE DATETIME, TIMEPERFORMED DATETIME);""")
	c.execute("""CREATE TABLE if not exists Workers ( WorkerID INT NOT NULL,WorkerName TEXT NOT NULL,WorkerDescription TEXT NOT NULL);""")
	c.execute("SELECT * FROM Assets")
	print ("Table created")
	conn.close()

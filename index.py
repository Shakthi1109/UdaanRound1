import os
import dbandtablecreate as db
import assetsall
import taskinsertion
import assetinsertion
import workerinsertion
import readallocate
import workerIDsearch
from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)
db.create()


@app.route('/add-asset',methods=['POST','GET'])
def addassest():
	if request.method == 'GET':
		return render_template('/addassets.html')
	if request.method == 'POST':
		ix=request.form['id']
		name=request.form['name']
		describe=request.form['describe']
		assetinsertion.insertTask(ix,name,describe)
		return render_template('/addassets.html',done="done")

@app.route('/add-task',methods=['POST','GET'])
def addtask():
	done=None
	if request.method == 'GET':
		return render_template('/addtasks.html',done=done)
	if request.method == 'POST':
		ix=request.form['id']
		name=request.form['name']
		describe=request.form['describe']
		taskinsertion.insertTask(ix,name,describe)
		return render_template('/addtasks.html',done="done")

@app.route('/add-worker',methods=['POST','GET'])
def addworker():
	if request.method == 'GET':
		return render_template('/addworker.html')
	if request.method == 'POST':
		ix=request.form['id']
		name=request.form['name']
		describe=request.form['describe']
		workerinsertion.insertTask(ix,name,describe)
		return render_template('/addworker.html',done="done")

@app.route("/asset/all",methods=['GET'])
def allassets():
	d=assetsall.readAssets()
	return render_template('assetall.html',parent_dict=d)

@app.route('/allocate-task',methods=['POST','GET'])
def allocatetask():
	if request.method == 'GET':
		return render_template('/allocatetask.html')
	if request.method == 'POST':
		asset=request.form['asset']
		task=request.form['task']
		worker=request.form['worker']
		timefirst=request.form['timefirst']
		timesecond=request.form['timesecond']
		readallocate.readallocate(worker,task,asset,timefirst,timesecond)
		return render_template('/allocatetask.html',done="done")

@app.route('/get-tasks-for-worker/<workerid>',methods=['GET'])
def getworkerbyid(workerid):
	d=workerIDsearch.readAssets(workerid)
	return render_template('/wordisp.html',dict_item=d)

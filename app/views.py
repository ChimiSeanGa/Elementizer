from flask import url_for, request, session, redirect, render_template, flash
from app import app
from periodic import getElemList, getElemNameList

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/elementize")
def elementize():
	input_str = request.args.get('input')
	words = input_str.split()
	numWords = len(words)
	elemList = []
	i = 0
	for w in words:
		i += 1
		l = getElemNameList(getElemList(w))
		if l == None:
			elemList = None
			break
		elemList.append(l)
		if i < numWords:
			elemList.append(None)
	print str(elemList)
	return render_template('elementize.html', 
		elemList=elemList)

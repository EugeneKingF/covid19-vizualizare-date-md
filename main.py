from flask import Flask , request , abort , redirect , Response ,url_for, render_template, session, request, jsonify
from flask import send_file, make_response, flash
import os, json, string
import shutil, glob, datetime
import sys
import io
import argparse

from scripts.sheets import SheetReader
from scripts.timeline_table import extract_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'saaa'


@app.route('/resetdata', methods=['GET'])
def reset():    
    x = SheetReader()
    data = x.getAllSheetDataRaw("covid")
    with open('data/minister.txt', 'w') as outfile:
    	json.dump(data, outfile)
    data = x.getAllSheetDataRaw("intrebari")
    with open('data/intrebari.txt', 'w') as outfile:
    	json.dump(data, outfile)
    data = x.getAllSheetDataRaw("timeline")
    with open('data/timeline.txt', 'w') as outfile:
    	json.dump(data, outfile)
    data = x.getAllSheetDataRaw("cuvinte")
    with open('data/cuvinte.txt', 'w') as outfile:
    	json.dump(data, outfile)
    return 'done'

def readData():
	with open('data/minister.txt') as json_file:
		mn = json.load(json_file)
	data = {}
	for k in mn[-1]:
		data[k] = mn[-1][k]
		data['y_'+k] = [i[k]  for i in mn]
	data['zile'] = len({i.split('/2020')[0]:1 for i in data['y_data']})
	return data

@app.route('/', methods=['GET'])
def index():
	data  = readData()
	return render_template('index3.html', data=data)

@app.route('/intreaba', methods=['GET'])
def ask():
	data  = []#readData()
	return render_template('ask.html', data=data)

@app.route('/intrebari-frecvente', methods=['GET'])
def qanda():
	data  = []#readData()
	return render_template('qanda.html', data=data)

@app.route('/datelazi', methods=['GET'])
def datelazi():
	data  = []#readData()
	return render_template('index3.html', data=data)

@app.route('/land', methods=['GET'])
def land():
	data  = []#readData()
	return render_template('land.html', data=data)

@app.route('/timeline', methods=['GET'])
def timeline():
	data  = extract_data()
	return render_template('includes/timeline.html', data=data)

@app.route('/data', methods=['GET'])
def data():
	data  = readData()
	return jsonify(data)

def getA():
    parser = argparse.ArgumentParser(description='Test a network')
    parser.add_argument('--live', dest='live',
                help='file to load the db state', default=False, type=bool)
    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = getA()
    pars = vars(args)
    if pars['live']:
        app.run(host='0.0.0.0', port=80, debug =True)
    else:
        app.run(host='0.0.0.0', port=6001, debug =True)

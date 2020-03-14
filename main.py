from flask import Flask , request , abort , redirect , Response ,url_for, render_template, session, request, jsonify
from flask import send_file, make_response, flash
import os, json, string
import shutil, glob, datetime
import sys
import io

import argparse

from scripts.sheets import getData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'saaa'


@app.route('/', methods=['GET'])
def index():
    data = getData()
    return render_template('index.html', data=data)

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
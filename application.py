from flask import Flask,jsonify
import urllib.request as request
import json
import pymysql
import pyodbc
#from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app)
countries=[]

@app.route("/name")
def country_name():
    c_name=[]
    with request.urlopen('https://restcountries.eu/rest/v2') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
        for i in data:
            dic={}
            dic['name']=i['name']
            dic['flag']=i['flag']
            c_name.append(dic)
    return jsonify(c_name)
            
@app.route("/capital")
def country_capital():
    c_capital=[]
    with request.urlopen('https://restcountries.eu/rest/v2') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
        for i in data:
            dic={}
            dic['capital']=i['capital']
            dic['flag']=i['flag']
            dic['name']=i['name']
            c_capital.append(dic)
    return jsonify(c_capital)
@app.route("/code")
def country_code():
    c_code=[]
    with request.urlopen('https://restcountries.eu/rest/v2') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
        for i in data:
            dic={}
            dic['code']=str(i['callingCodes'][0])
            dic['flag']=i['flag']
            dic['name']=i['name']
            c_code.append(dic)
    return jsonify(c_code)
@app.route("/continent")
def country_continent():
    c_continent=[]
    with request.urlopen('https://restcountries.eu/rest/v2') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
        for i in data:
            dic={}
            dic['region']=i['region']
            dic['flag']=i['flag']
            dic['name']=i['name']
            c_continent.append(dic)
    return jsonify(c_continent)


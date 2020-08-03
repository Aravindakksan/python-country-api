from flask import Flask,jsonify
import urllib.request as request
import simplejson 
import json
import pymysql
import pyodbc
#from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app)
countries=[]
# Connect to the database
server = 'tcp:country.database.windows.net' 
database = 'rest country api' 
username = 'aravind' 
password = 'Akksan766764#'
connection = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor()
cursor.execute("SELECT * FROM country")
rows = cursor.fetchall()
rows=list(rows)


key=('name','code','capital','region','subregion','population','area','lat','lon','timezone','currency','flag')
for i in range(len(rows)):
    country={}
    for j in range(len(rows[i])):
        t=key[j]
        country[t]=rows[i][j]
    countries.append(country)


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

@app.route("/")
def home():
    name=[]
    ccode=[]
    capital=[]
    region=[]
    subregion=[]
    population=[]
    area=[]
    latlong=[]
    timezone=[]
    currency=[]
    flag=[]

    with request.urlopen('https://restcountries.eu/rest/v2') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
        for i in range(0,len(data)):
            name.append(data[i]['name'])
            ctemp=str(data[i]['callingCodes'][0])
            ccode.append(ctemp)
            capital.append(data[i]['capital'])
            region.append(data[i]['region'])
            subregion.append(data[i]['subregion'])
            population.append(data[i]['population'])
            if(str(data[i]['area'])=='None'):
                area.append(0)
            else:
                area.append(data[i]['area'])
            if(data[i]['latlng']==[]):
                latlong.append([0,0])
            else:    
                latlong.append(data[i]['latlng'])
            ttemp=(str(data[i]['timezones'][0]))
            timezone.append(ttemp)
            currency.append(data[i]['currencies'][0]['name'])
            flag.append(data[i]['flag'])

    
    # Create a new record
    if(len(rows)<250):
        for i in range(0,len(name)):
            cursor.execute("INSERT INTO dbo.country(name,code,capital,region,subregion,population,area,lat,lon,timezone,currency,flag) values (?,?,?,?,?,?,?,?,?,?,?,?)", name[i],str(ccode[i]),capital[i],region[i],subregion[i],str(population[i]),str(area[i]),str(latlong[i][0]),str(latlong[i][1]),timezone[i],currency[i],flag[i])
            connection.commit()

    print(len(rows))
    return jsonify(countries)
    

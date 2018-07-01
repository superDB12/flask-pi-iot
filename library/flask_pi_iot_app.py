from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests
from library.pi_iot_data import pi_iot_data as piData

app = Flask(__name__)

data = piData.piIotData()

@app.route('/test', methods=['POST','GET'])
def my_test():
    if request.method == "POST":
        print("/test")
        print("This is what is in the request object: ")
        print(request)
        print("Here's what's in the request.form:  ")
        print(request.form)
        d = request.form
        data.add_reading(d["serial-no"], d["timestamp"], d["x"], d["y"], d["z"])
        print(data.get_number_readings())
        return("Data added")
    return("Test page")

@app.route('/yaml')
def my_yaml_microservice():
    pass
    #return ymlify({'Hello':'World'})


@app.route('/')
@app.route('/index.html')
def main_page():
    return render_template('index.html')

@app.route('/johnpi.html',methods=['POST','GET'])
def john_page():
    if request.method == 'POST':
        print("JohnPi got a post")
        print(request.form)
    return render_template('johnpi.html')

@app.route('/meganpi.html',methods=['POST','GET'])
def megan_page():
    if request.method == 'POST':
        print("MeganPi got a post")
        print(request.form)
    return render_template('meganpi.html')


@app.route('/katiepi.html',methods=['POST','GET'])
def katie_page():
    if request.method == 'POST':
        print("KatiePi got a post")
        print(request.form)
    return render_template('katiepi.html')

@app.route('/davidpi.html',methods=['POST','GET'])
def david_page():
    if request.method == 'POST':
        print("DavidPi got a post")
        print(request.form)
    return render_template('davidpi.html')

@app.route('/alldata.html',methods=['POST','GET'])
def alldata_page():
    if request.method == 'POST':
        pass
    print("All Data got a GET")
    d=data.get_readings()
    print(d)
    return render_template('alldata.html', data = d)
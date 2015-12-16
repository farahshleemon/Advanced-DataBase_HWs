from flask import Flask, render_template, request, jsonify
from flask.ext.responses import json_response, xml_response, auto_response
import json
from MongoRotines import *

update=0;
app = Flask(__name__)

# Generate a secret random key for the session
conn = MongoClient()
db = conn.Project
CrimeTable = db.CrimeTable


@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/delete')
def start_delete_page():
    
    return render_template('delete.html')

@app.route('/edit')
def start_edit_page():
    return render_template('Edit.html')

@app.route('/new')
def start_new_page():
    return render_template('new.html')
@app.route('/BarChart')
def start_BarChart_page():
    return render_template('barchart.html')
@app.route('/QBY')
def Start_Query_By_Year_page():
    return render_template('QueryByYear.html')

@app.route('/post', methods = ['POST'])
def post():
    # Get the parsed contents of the form data    
    obj = request.json    
    new_item(obj)
    return jsonify(obj)

@app.route('/Deletepost', methods = ['POST'])
def Deletepost():
    # Get the parsed contents of the form data    
    obj = request.json
    
    discard_item(obj)
    return jsonify(obj)
@app.route('/Editpost', methods = ['POST'])
def Editpost():
    # Get the parsed contents of the form data
    global update
    obj = request.json
    print obj
    dict1=find_item(obj)
    update=dict1['_id']
    data = {}
    for key in dict1:
        data[str(key)] = str(dict1[key])    
    return jsonify(data)

@app.route('/postUpdate', methods = ['POST'])
def postUpdate():
    # Get the parsed contents of the form data    
    obj = request.json    
    update_item(obj,update)
    return jsonify(obj)

@app.route('/peryear')
def peryear():
    dic=Number_of_Crimes_each_year()
    return jsonify(dic)
@app.route('/peryear2')
def peryear2():
    dic=Number_of_Crimes_each_year()
    dic2=Number_of_Arrest_each_year()
    dicall={}
    dicall["c"]=dic
    dicall["a"]=dic2
    return jsonify(dicall)
@app.route('/Yearpost', methods = ['POST'])
def Yearpost():
    # Get the parsed contents of the form data
    global update
    obj = request.json
    year=obj['Year']    
    list=queryByYear(year)
    dict1={}
    dict1["r"]=str(list)
    return jsonify(dict1)
    
if __name__ == '__main__':
	app.run( 
		host="localhost",
		port=int("8001")
	)

from flask import Flask,jsonify, request
from functions import *
from  main_exe import * 


app = Flask(__name__)

@app.route("/")
def welcome() : 
    return "Hello"

@app.route("/add_leave", methods=['POST'])
def add_leave_route():
    request_data = request.get_json()
    print(request_data)
    description = request_data['description1']
    start_date = request_data['start_date1']
    end_date = request_data['end_date1']
    result = add_val(description, start_date , end_date)
    return str(result)

@app.route("/approve_leave/<int:id>", methods=['GET'])
def approve_leave_route(id):
    request_data = request.get_json()
    print(request_data)
    id = request_data['ID']
    result = approve_leave(id)
    return jsonify(result)


@app.route("/reject_leave/<int:id>", methods=['GET'])
def reject_leave_route(id):
    request_data = request.get_json()
    print(request_data)
    id = request_data['ID']
    result = reject_leave(id)
    return jsonify(result)

@app.route("/delete_value/<int:id>", methods=['DELETE'])
def delete_value_route(id):
    request_data = request.get_json()
    print(request_data)
    id = request_data['ID']
    result = delete_value(id)
    return jsonify(result)


@app.route("/display_table")
def display_route():

    result= display_table()
    return str(result)


@app.route("/status/<int:id>")
def route5(id):
    cur.execute("SELECT status FROM leave_system_management WHERE id=%s;", id)
    result = cur.fetchone()

    if result:
        return result[0]
    else:
        return "ID not found"


if(__name__=="__main__"):
    app.run(debug = True)
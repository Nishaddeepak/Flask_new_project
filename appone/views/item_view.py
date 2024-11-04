from flask import request, jsonify
from appone.controllers import item_controller
from appone import app
@app.route("/create_app", methods=["POST"])
def create_app():
    data=request.get_json()
    res=item_controller.con_create_emp(data)

@app.route("/fetch_emp/<id>", methods=["GET"])
def emp_details(id):
    res=item_controller.con_fetch(id)
    return jsonify(message=res)

@app.route("/update/<id>", methods=["PUT"])
def updating_emp(id):
    data=request.get_json()
    res=item_controller.con_update(id, data)
    return jsonify (message="res")

@app.route("/delete/<id>", methods=["DELETE"])
def del_emp(id):
    res=item_controller.con_del_emp(id)
    return jsonify (message=res)
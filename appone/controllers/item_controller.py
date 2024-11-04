from appone.models.item_model import Registertable
from appone import db


def con_create_emp(data):
    emp=Registertable.query.filter_by(name=data["name"]).first()
    if emp:
        return "Employee is already exist"
    db_emp=Registertable(name=data["name"], email=data["email"], position= data["position"])
    db.session.add(db_emp)
    db.session.commit()
    return "Employee added successfully"

def con_fetch(id):
    emp=Registertable.query.get(id)
    if emp:
        res={"id":emp.id, "name":emp.name, "email":emp.email, "position":emp.position}
        return res
    return "employee not found"

def con_update(id, data):
    emp=Registertable.query.get(id)
    if emp:
        emp.name=data["name"]
        emp.email=data["email"]
        emp.position=data["position"]
        db.session.commit()
        return "Employee details updated succesfully"
    return "provide valid id"

def con_del_emp(id):
    emp=Registertable.query.get(id)
    if emp:
        db.session.delete(emp)
        db.session.commit()
        return "eployee deleted successfully"
    return "provide valid details"

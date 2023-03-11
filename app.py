from flask import Flask,Response,render_template,request ,url_for,redirect# flasks 
from pymongo import MongoClient # mongodb 
from bson.objectid import ObjectId # json like bason
import json
import requests
app = Flask(__name__)

client = MongoClient('localhost', 27017) # connection 
db = client.API # create table
myapis = db.apis # triger




@app.route('/',methods=['GET'])
def Home():
    data = list(myapis.find())

    # serialize the id 
    for user in data:
         user["_id"]=str(user["_id"])

    Message = Response(response=json.dumps(
                {"Message":"Display All Users",
                "Payload":data,
                "Status":200}),
            status=201,
            mimetype ="application/json")

    return Message



@app.route('/add',methods=['POST'])
def adduser():
    User={"name":"Amitab","last name":"Bachchan"}
    dbResponse = myapis.insert_one(User)

    Message = Response(
                response=json.dumps(
                    {"Message":"Add Data Succesfully ",
                    "Payload":f'id : {dbResponse.inserted_id}',
                    "Status":200}),
                status=201,
                mimetype ="application/json")
    return Message



@app.route('/update/<id>',methods=['PATCH'])
def updateuser(id): 
    updateuserdata =myapis.update_one(
            {'_id':ObjectId(id)},
            {'$set':{"name":request.form['name']}}
            )
    Message = ({"Status":200,"Payload":id,"Message":"Data Updated "})
    return Message

@app.route('/delete/<id>',methods=['DELETE'])
def deleteuser(id):
    deleteuserdata = myapis.delete_one(
            {'_id':ObjectId(id)},
            )
    Message = ({"Status":200,"Payload":id,"Message":"Delete Items  "})
    return Message




@app.errorhandler(404)
def error404(error=None):
    Message = Response(response=json.dumps(
        {
        'Status':404,
        'Message':'Page Not Found '
        }),
        status=400)
    print("******  Error  *******")
    return Message




# _______run_________________
if __name__=='__main__':
    app.run(debug=True)
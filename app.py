from flask import Flask,render_template,request ,url_for,redirect # flasks 
from pymongo import MongoClient # mongodb 
from bson.objectid import ObjectId # json lke bason

app = Flask(__name__)

client = MongoClient('localhost', 27017) # connection 

db = client.ToDoDB # create table
todos = db.todos # triger


#functin 
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)



@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))






if __name__=='__main__':
    app.run(debug=True)

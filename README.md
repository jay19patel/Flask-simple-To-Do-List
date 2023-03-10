# Flask-simple-To-Do-List
- create venv 
- pip install flask

- import flask 
- set flask in  variabe  app
    app = Flask(__name__)

- create route for navigae urls 
    @app.route('/')

- create function for logic and page rendering 
    def hellow():
        return 'hellow'

- run the site :
    if __name__ =='__main__':
        app.run(debug=True)

        debug means if have any error than degub true is for display error in brouser 

- if you need render html page then import render_template from flask
 - add the render in rentern and add file path using static 
    ex:
    @app.route('/')
    def hellow():
        return render_template('index.html')

- create own html page (like bootstrap to do list )

----create model in flask(database tables)-----
- create connecttion with data base:
    install pymongo
        pip install Flask pymongo
        import : from pymongo import MongoClient

- client= MongoClient('localhost', 27017)
- create document :
    db = client.FileName # create table
    dbdata = db.Collectioname # triger


- create class 
    class Todo(db.Model):
        sno =db.Column(db.Integer,primary_key=True)
        title = db.Column(db.String(100), unique=True, nullable=False)
        
        
        
        ![img1](https://user-images.githubusercontent.com/107461719/224266677-d5c119bc-ad50-4031-8317-c4a75852744c.PNG)
![image](https://user-images.githubusercontent.com/107461719/224266841-f815697f-6aa8-4567-9db6-f839ae4ab521.png)

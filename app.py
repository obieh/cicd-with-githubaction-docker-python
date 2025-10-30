from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)    

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    complete= db.Column(db.Boolean)
    


@app.route('/edit') 
def base():
    todo_list=Todo.query.all()
    return render_template('index.html', todo_list=todo_list)



@app.route('/') 
def list():
    todo_list=Todo.query.all()
    return render_template('list.html', todo_list=todo_list)


if __name__ == '__main__':
    app.run()
   
   

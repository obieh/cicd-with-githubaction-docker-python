# CICD-with-github action-docker-python
### This project demonstrates how to use python, docker, github-actions to build devops pipeline.

* Build a simple webapp with HTML, CSS & Bootstrap.

* Add DB with SQL-Alchemy

* Expose our app to the public

* Test with pytest & selenuim

* Push all codes to github repo

* Create CICD server with uthubaction

* Build docker file and create a docker repository.

* Optional kubernetes to handle Multiple containers

### Set up virtual environment.

1. Setup python virtual environment run `python3 -m virtualenv cicd`

![](./img/Pasted%20image.png)

2. Activate the virtual env, run `source cicd/bin/activate`

![](./img/Pasted%20image%20(2).png)

### Your terminal should switch to the venv folder in brackets at the beginingof the terminal, as show above.

3. Install flask framework run `pip3 install flask` while on the venv.

![](./img/Pasted%20image%20(3).png)

4. Create a requirement text file in your venv. The essence is to add all the requirements into the text file and runn all at once instead of running individually.

5. Add 'Flask, SQLAlchemy, Flask-SQLAlchemy and pytest" into the text file.

![](./img/Pasted%20image%20(4).png)

6. Run `pip install -r .cicd/requirement.txt` to install all the listed requirements in the text file.

![](./img/Pasted%20image%20(5).png)

7. (Optional) You can run `pip3 freeze` to get a list of requirements installed on your venv.

![](./img/Pasted%20image%20(6).png)

8. Create first app. Add a app.py file.

```python
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!" 

if __name__ == '__main__':
    app.run()
```
9. Run the flask app.

![](./img/Pasted%20image%20(7).png)

10. On your browser, copy and paste `http://127.0.0.1:5000` to verify your app is running.

![](./img/Pasted%20image%20(8).png)

11. Create a new folder named 'templates', In the new folder, create an index.html file.

12 Add a basic html page as below.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Base</title>
</head>
<body>
    <h1> Hi Everyone, this message is from Base</h1>
</body>
</html>
```
13. Update the code in app.py to look as below

```python
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!" 


@app.route('/base') 
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
```
14. Run the app again. `python3 app.py`

![](./img/Pasted%20image%20(9).png)

### There is a function naming comflict as shown.

15. Change the base route function name form home to base.

![](./img/Pasted%20image%20(10).png)

16. Run the app agian

![](./img/Pasted%20image%20(11).png)

17. Go to your browser type `127.0.0.1:5000` to verify your app is running.

![](./img/Pasted%20image%20(12).png)

### Add Database, create class && update pages. 
* Update app.py 
```python
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
   
```

### Add CRUD function.

* Update app.py as below.

```python

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)    

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    complete = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        new_todo = Todo(content=title, complete=False)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

# toggle completion (keeps name 'update' to match existing links)
@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        todo.complete = not todo.complete
        db.session.commit()
    return redirect(url_for('index'))

# delete
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('index'))

# Edit route: GET shows form, POST saves edited content
@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return redirect(url_for('index'))

    if request.method == 'POST':
        new_content = request.form.get('title')
        if new_content:
            todo.content = new_content
            db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', todo=todo)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

```
* Go to your browser to test the routes. You may need to restart the server.
![](./img/Pasted%20image%20(13).png)

* Test the add route, type tasks and click add.
![](./img/Pasted%20image%20(14).png)

* Test complete function. Click complet on any task.

![](./img/Pasted%20image%20(16).png)

* Test delete route.

![](./img/Pasted%20image%20(17).png)
### The other tasks was deleted successfully.

### Server logs on terminal.

![](./img/Pasted%20image%20(15).png)

### Add test case for the app.

1. Create a new file in the project directory, name it test.py and add the code below.

```python
from app import app, db, Todo
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        t = Todo(content='sample task', complete=False)
        db.session.add(t)
        db.session.commit()
        client = app.test_client()
        yield client
        db.session.remove()
        db.drop_all()

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_edit_page(client):
    # ensure the edit page for the created todo returns 200
    with app.app_context():
        todo = Todo.query.first()
        assert todo is not None
        resp = client.get(f'/edit/{todo.id}')
        assert resp.status_code == 200
```

2. Run `pytest -q test.py`

![](./img/Pasted%20image%20(18).png)

### Indeed the two test cases in our test.py passed.
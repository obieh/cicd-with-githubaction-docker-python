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


   


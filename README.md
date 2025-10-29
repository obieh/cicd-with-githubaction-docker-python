# CICD-with-githubaction-docker-python
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




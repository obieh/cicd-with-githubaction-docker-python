from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!" 


@app.route('/base') 
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
   
   

from flask import Flask
app = Flask(__name__)


@app.route('/user/<name>')
def my_user(name):
    return "Hello %s Welcome" % name


app.run(debug=True)

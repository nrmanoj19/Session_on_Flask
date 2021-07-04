from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello Team</h1>"


@app.route('/hello/<user>')
def hello_user(user):
    return render_template('hello.html', name=user)


app.run(debug=True)

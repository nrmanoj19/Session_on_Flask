from flask import Flask
app = Flask(__name__)


@app.route('/user/<name>')
def my_user(name):
    return "Hello %s Good evening" % name


@app.route('/user/<name>/age/<int:age>')
def my_age(name, age):
    return "Hello %s your age is %d" % (name, age)


@app.route('/user/<name>/age/<int:age>/experience/<float:exp>')
def my_exp(name, age, exp):
    return "Hello %s your age is %d and your experience is %.2f" % (name, age, exp)


app.run(debug=True)







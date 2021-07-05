from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello My New World"


app.run(debug=True)


# def hello_world():
#    return "hello world"
#
#
# app.add_url_rule(‘/’, "hello", hello_world)

from flask import Flask, request
app = Flask(__name__)


@app.route('/add_get', methods=['GET'])
def my_addition():
    my_num1 = int(request.args.get('num1'))
    my_num2 = int(request.args.get('num2'))
    return str(my_num1 + my_num2)


app.run(debug=True)

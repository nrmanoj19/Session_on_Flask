from flask import Flask, request
app = Flask(__name__)


@app.route('/add_post', methods=['POST'])
def my_addition():
    my_body = request.json
    my_res = my_body['num1'] + my_body['num2']
    return str(my_res)


if __name__ == '__main__':
    app.run(debug=True)

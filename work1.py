from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/add_get', methods=['GET'])
def my_details():
    my_name = (request.args.get('name'))
    my_age = (request.args.get('age'))
    my_mailid = (request.args.get('mailid'))
    total=str(my_name + my_age+ my_mailid)
    return json.dumps(total)

app.run(debug=True)
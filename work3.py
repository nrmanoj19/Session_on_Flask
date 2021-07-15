from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/add_post', methods=['POST'])
def my_details():
    my_body = request.json
    my_res = my_body['name'] + str(my_body['age']) + my_body['mailid']
    #my_res = my_body['name']
    return json.dumps(my_res)

app.run(debug=True)



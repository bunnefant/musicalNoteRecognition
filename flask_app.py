from flask import Flask
from flask import request
from flask_cors import CORS
import json
app = Flask(__name__)
cors = CORS(app)
name = ''

@app.route("/")
def home():
    print(name)
    return json.dumps(name)

@app.route("/postData", methods = ['POST'])
def setData():
    global name
    print(request.get_json())
    name = request.get_json()['data']
    # name['h'] = request.form.
    return request.get_json()


if __name__ == "__main__":
    app.run()

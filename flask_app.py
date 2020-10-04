from flask import Flask
from flask import request
from flask_cors import CORS
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType
import json
import matlab.engine

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
    name = request.get_json()['name']
    # name['h'] = request.form.
    # matlabEngine = matlab.engine.start_matlab()
    # matlabEngine.pyth(float(3),float(5)) #runs matlab function in the MATLAB directory
    # matlabEngine.quit()
    return request.get_json()


if __name__ == "__main__":
    app.run()

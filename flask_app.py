from flask import Flask
from flask import request
from flask_cors import CORS
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType
import json
# import matlab.engine

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
    # print(request.get_json())
    path = "C:/Users/bunne/Desktop/hackathons/musicalNoteRecognition"


    # name['h'] = request.form.
    # matlabEngine = matlab.engine.start_matlab()
    # matlabEngine.pyth(float(3),float(5)) #runs matlab function in the MATLAB directory
    # matlabEngine.quit()

    config = {
        'host':'identify-eu-west-1.acrcloud.com',
        'access_key':'945a4fef66492f6361dfb80ce4b00bb0',
        'access_secret':'Dl7hpMntRyRBDl6UHNHyKoiGMIgXRn0gvpciDSFQ',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug':False,
        'timeout':10 # seconds
    }

    '''This module can recognize ACRCloud by most of audio/video file.
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].

    if request.get_json()['upload'] == 1:
        name = request.get_json()['name']
        song = json.loads(re.recognize_by_file(name, 10, 20))
        title = song['metadata']['music'][0]['title']
        # print(json.loads(song))
        # print(title)
        artist = song['metadata']['music'][0]['artists'][0]['name']
        # print(title + " by " + artist)
        matlabEngine.cd(path)
        freq, time = matlabEngine.convertMP3(name, nargout=2)
        # print(freq)
        # print(time)
        matlabEngine.quit()
        return {"identify" : title + " by " + artist, "freq" : freq, "time" : time}
    else:
        f = open("music67.mp3", "w")
        f.write(request.get_json()['data'])
        f.close()
        # buf = open("music67.mp3", 'rb').read()
        # recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
        song = json.loads(re.recognize_by_file("music67.mp3", 0, 10))
        print(song)
        # title = song['metadata']['music'][0]['title']
        # artist = song['metadata']['music'][0]['artists'][0]['name']
        # return {"identify" : title + " by " + artist}
        return {'hello' : 'hello'}

if __name__ == "__main__":
    app.run()

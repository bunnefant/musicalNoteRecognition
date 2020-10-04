
import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType
import json

if __name__ == '__main__':
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
    song = json.loads(re.recognize_by_file("music1.mp3", 10, 20))
    title = song['metadata']['music'][0]['title']
    # print(json.loads(song))
    # print(title)
    artist = song['metadata']['music'][0]['artists'][0]['name']
    print(title + " by " + artist)

    #print("duration_ms=" + str(ACRCloudRecognizer.get_duration_ms_by_file("music1.mp3")))

    buf = open("music1.mp3", 'rb').read()
    # recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    print(re.recognize_by_filebuffer(buf, 0, 10))

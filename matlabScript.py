import matlab.engine
matlabEngine = matlab.engine.start_matlab()



#
# with open("myScript.m","w+") as f:
#     f.write(code)
path = "C:/Users/bunne/Desktop/hackathons/musicalNoteRecognition"
# eng.addpath(r'C:\Users\bunne\Desktop\hackathons\musicalNoteRecognition\matlabCode',nargout=0)
# matlabEngine.evalc('cd C:\Users\bunne\Desktop\hackathons\musicalNoteRecognition')
matlabEngine.cd(path)
notes, octave, time = matlabEngine.convertMP3("Giorno's Theme but it's actually the best part played on piano.mp3", nargout=3)
print(notes)
print(list(time._data))
print(list(octave._data))
matlabEngine.quit()

import matlab.engine
matlabEngine = matlab.engine.start_matlab()



#
# with open("myScript.m","w+") as f:
#     f.write(code)
path = "C:/Users/bunne/Desktop/hackathons/musicalNoteRecognition"
# eng.addpath(r'C:\Users\bunne\Desktop\hackathons\musicalNoteRecognition\matlabCode',nargout=0)
# matlabEngine.evalc('cd C:\Users\bunne\Desktop\hackathons\musicalNoteRecognition')
matlabEngine.cd(path)
print(matlabEngine.convertMP3("2020-2021 TMEA Trumpet Etude 1 D major - Con Fuoco.mp3"))
matlabEngine.quit()

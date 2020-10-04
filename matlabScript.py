import matlab.engine
matlabEngine = matlab.engine.start_matlab()



#
# with open("myScript.m","w+") as f:
#     f.write(code)

# eng.addpath(r'C:\Users\bunne\Desktop\hackathons\musicalNoteRecognition\matlabCode',nargout=0)
# matlabEngine.evalc('cd C:\Users\bunne\Desktop\hackathons\musicalNoteRecognition')
# matlabEngine.cd(r'C:\Users\bunne\Desktop\hackathons\musicalNoteRecognition')
print(matlabEngine.pyth(float(3),float(5)))
matlabEngine.quit()

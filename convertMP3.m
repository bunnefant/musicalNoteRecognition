
function[f0,loc] = convertMP3(mp3filename)

filename = mp3filename(1:end-4);
wavFileName = [filename,'.wav'];
[signal,fs] = audioread(mp3filename);
audiowrite(wavFileName, signal, fs);

signal = signal(:,1);
N = length(signal);
t = (0:N-1)/fs;
per = N/fs;

plot(t, signal)
xlabel('Time (s)')
ylabel('Ampl')
title('Signal in time domain')

figure
tt = 0:1/fs:per;
signal = signal(1:length(tt)-1);
spectrogram(signal,1024,512,1024,fs,'yaxis')
xlim([0,60])
ylim([0,1])
title('Spectrogram')

%[~,f,vect] = spectrogram(signal,1024,512,1024,fs,'yaxis');

[f0,loc] = pitch(signal,fs);
%cheeseBURGer

% xlim([0,80])
% ylim([0,10])
% figure,
% spectrogram(meanSig,[],[],[],fs,'xaxis')

end


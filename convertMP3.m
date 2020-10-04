
function[noteV,octiveV,timeV] = convertMP3(mp3filename)
filename = mp3filename(1:end-4);
wavFileName = [filename,'.wav'];
[signal,fs] = audioread(mp3filename);
audiowrite(wavFileName, signal, fs);

signal = signal(:,1);
N = length(signal);
t = (0:N-1)/fs;
per = N/fs;

% plot(t, signal)
% xlabel('Time (s)')
% ylabel('Ampl')
% title('Signal in time domain')

% figure
tt = 0:1/fs:per;
signal = signal(1:length(tt)-1);
% spectrogram(signal,1024,512,1024,fs,'yaxis')

% xlim([0,per])
% ylim([0,2])
% title('Spectrogram')


[f0,loc] = pitch(signal,fs);

o = 0;
[oct,fvec] = helpfindoctave(f0,o);
[noteV,octiveV,timeV] = choosepitch(fvec,oct,loc);

end


function [octvec,fvec] = helpfindoctave(f,o)
o = 0;
octvec = [];
fvec = [];
for x = 1:length(f)
    if f(x) >= 254.284 &  f(x) <= 508.5675
        fout = f(x);
        oct = o;
    elseif f(x) < 254.284
        fout = f(x);
        oct = o;
        while fout < 254.284
            fout = 2*fout;
            oct = oct - 1;
        end
    elseif f(x) > 508.5675
        fout = f(x);
        oct = o;
        while fout > 508.5675
            fout = fout/2;
            oct = oct + 1;
        end
    end
octvec = [octvec; oct];
fvec = [fvec; fout];
end
end

function [notevec,octvec,locvec] = choosepitch(f0,oct,loc)

octvec = [];
notevec = [];
locvec = [];
maskvec = [];

if f0(1) >= 254.284 & f0(1) < 269.4045
        p = "C";
    elseif f0(1) >= 269.4045 & f0(1) < 285.424
        p = "C#";
    elseif f0(1) >= 285.424 & f0(1) < 302.396
        p = "D";
    elseif f0(1) >= 302.396 & f0(1) < 320.3775
        p = "Eb";
    elseif f0(1) >= 320.3775 & f0(1) < 339.428
        p = "E";
    elseif f0(1) >= 339.428 & f0(1) < 359.611
        p = "F";
    elseif f0(1) >= 359.611 & f0(1) < 380.9945
        p = "F#";
    elseif f0(1) >= 380.9945 & f0(1) < 403.65
        p = "G";
    elseif f0(1) >= 403.65 & f0(1) < 427.6525
        p = "Ab";
    elseif f0(1) >= 427.6525 & f0(1) < 453.082
        p = "A";
    elseif f0(1) >= 453.082 & f0(1) < 480.0235
        p = "Bb";
    elseif f0(1) >= 480.0235 & f0(1) < 508.567
        p = "B";
    else
        error('frequency outside of acceptable range')
end
    notevec = [notevec; p];
    octvec = [octvec; oct(1)];
    locvec = [locvec; loc(1)];
    maskvec = [maskvec, false];


for x = 2:length(f0)
    f1 = f0(x);
    if f1 >= 254.284 & f1 < 269.4045
        p = "C";
    elseif f1 >= 269.4045 & f1 < 285.424
        p = "C#";
    elseif f1 >= 285.424 & f1 < 302.396
        p = "D";
    elseif f1 >= 302.396 & f1 < 320.3775
        p = "Eb";
    elseif f1 >= 320.3775 & f1 < 339.428
        p = "E";
    elseif f1 >= 339.428 & f1 < 359.611
        p = "F";
    elseif f1 >= 359.611 & f1 < 380.9945
        p = "F#";
    elseif f1 >= 380.9945 & f1 < 403.65
        p = "G";
    elseif f1 >= 403.65 & f1 < 427.6525
        p = "Ab";
    elseif f1 >= 427.6525 & f1 < 453.082
        p = "A";
    elseif f1 >= 453.082 & f1 < 480.0235
        p = "Bb";
    elseif f1 >= 480.0235 & f1 < 508.567
        p = "B";
    else
        error('frequency outside of acceptable range')
    end
    notevec = [notevec; p];
    mask1 = strcmp(notevec(x-1),notevec(x));
    maskvec = [maskvec, mask1];
    octvec = [octvec; oct(x)];
    locvec = [locvec; loc(x)];
end

mask2 = maskvec == 0;
notevec = notevec(mask2);
octvec = octvec(mask2);
locvec = locvec(mask2);

end

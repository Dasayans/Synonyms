import os
os.system('cls')
import wave
k=input()
with wave.open('sample-12s.wav', 'rb') as input_wave:
        sample_width = input_wave.getsampwidth()
        framerate = input_wave.getframerate()
        nframes = input_wave.getnframes()
        channels = input_wave.getnchannels()
        frames = input_wave.readframes(nframes)
with wave.open('sample-12sn.wav', 'wb') as output_wave:
    output_wave.setsampwidth(sample_width)
    output_wave.setframerate(framerate*k)
    output_wave.setnchannels(channels)
    output_wave.writeframes(frames)
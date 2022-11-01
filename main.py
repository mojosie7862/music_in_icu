import pyaudio
import wave
import keyboard
import time

filename = '3_tone_480.wav'

# Set chunk size of 1024 samples per data frame
chunk = 1024

# Open the sound file
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(chunk)

time.sleep(10)  #time to click over to recorder window

#baseline 5 mins
keyboard.send('1')
print('starting baseline 1')
time.sleep(10) #should be 300 seconds for trials

# Play the sound by writing the audio data to the stream
keyboard.send('2')
print('starting music')
while data != b'':
    stream.write(data)
    data = wf.readframes(chunk)
keyboard.send('3')
print('stopping music')

print('starting baseline 2')
time.sleep(10) #should be 300 seconds for trials
keyboard.send('4')
print("trial finished")

stream.stop_stream()
stream.close()
p.terminate()
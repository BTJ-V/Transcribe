import requests
import assemblyai as aai
from api_secrets import API_KEY_ASSY
import wave
import pyaudio
from playsound import playsound

FRAMES_PER_BUFFER = 3200
CHANNELS = 1
RATE = 16000
FORMAT = pyaudio.paInt16

p = pyaudio.PyAudio()

stream = p.open(frames_per_buffer=FRAMES_PER_BUFFER, channels=CHANNELS, rate=RATE, format=FORMAT, input=True)
print("start recording")
seconds = 3
frames = []
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)) :
data = stream. read(FRAMES_PER_BUFFER)
frames. append(data)
print("Command received. Processing the output...")
stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open('command.wav', 'wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj .writeframes(b"".join(frames))
obj.close()

aai.settings.api_key = API_KEY_ASSY
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("command.wav")
command = transcript.text
print(command)

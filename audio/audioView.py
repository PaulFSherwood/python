import pyaudio
import numpy as np
from blessed import Terminal
import time

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
AUDIO_DEVICE_INDEX = None  # Set this to your audio device index if needed

audio = pyaudio.PyAudio()

def start_stream():
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK, input_device_index=AUDIO_DEVICE_INDEX)
    return stream

def analyze_audio(stream):
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    peak = np.average(np.abs(data)) * 2
    bars = "#" * int(50 * peak / 2**16)
    return bars

term = Terminal()
stream = start_stream()

try:
    while True:
        audio_level = analyze_audio(stream)
        with term.location(0, 0):
            print(term.clear)
            print(f"Audio Level: {audio_level}")
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()


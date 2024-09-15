import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
from pydub import AudioSegment
from flask import Flask, jsonify

# Function to save the recorded audio as a WAV file
def save_wav(audio_data, sample_rate, filename='output.wav'):
    wavfile.write(filename, sample_rate, audio_data)
    print("Audio saved as {}".format(filename))

# Function to convert WAV file to MP3 using Pydub
def convert_to_mp3(wav_filename, mp3_filename='output.mp3'):
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(mp3_filename, format="mp3")
    print("Converted to MP3: {}".format(mp3_filename))


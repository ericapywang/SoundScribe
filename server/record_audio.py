import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
from pydub import AudioSegment
from flask import Flask, jsonify

# Function to record audio from the microphone
# @app.route('/api/record', methods=['GET'])
# def record_audio(duration=5, sample_rate=44100):
#     print("Recording for {} seconds...".format(duration), file=sys.stderr)
#     audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
#     sd.wait()  # Wait until the recording is finished

#     wav_filename = 'recorded_audio.wav'
#     save_wav(audio_data, sample_rate, wav_filename)

#     mp3_filename = 'recorded_audio.mp3'
#     convert_to_mp3(wav_filename, mp3_filename)

#     return audio_data, sample_rate

# Function to save the recorded audio as a WAV file
def save_wav(audio_data, sample_rate, filename='output.wav'):
    wavfile.write(filename, sample_rate, audio_data)
    print("Audio saved as {}".format(filename))

# Function to convert WAV file to MP3 using Pydub
def convert_to_mp3(wav_filename, mp3_filename='output.mp3'):
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(mp3_filename, format="mp3")
    print("Converted to MP3: {}".format(mp3_filename))

# def main():
#     # Record audio from the microphone
#     duration = 5  # Seconds
#     audio_data, sample_rate = record_audio(duration)

#     # Save as WAV file
#     wav_filename = 'recorded_audio.wav'
#     save_wav(audio_data, sample_rate, wav_filename)

#     # Convert WAV to MP3
#     mp3_filename = 'recorded_audio.mp3'
#     convert_to_mp3(wav_filename, mp3_filename)

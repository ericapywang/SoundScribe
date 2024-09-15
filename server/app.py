# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from record_audio import save_wav, convert_to_mp3
import sounddevice as sd

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

@app.route('/api/record', methods=['GET'])
def record_audio(duration=5, sample_rate=44100):
    print("Recording for {} seconds...".format(duration))
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is finished

    wav_filename = 'recorded_audio.wav'
    save_wav(audio_data, sample_rate, wav_filename)

    mp3_filename = 'recorded_audio.mp3'
    convert_to_mp3(wav_filename, mp3_filename)

    return audio_data, sample_rate

if __name__ == "__main__":
    app.run(debug=True, port=5000)

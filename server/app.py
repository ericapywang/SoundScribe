# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from record_audio import save_wav, convert_to_mp3
from transcribe import transcribe
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

    return ""

@app.route('/api/transcribe', methods=['GET'])
def transcribe_audio():
  print("transcribing audio")
  transcribe()

@app.route('/api/predict', methods=['GET'])
def predict():
  parser = argparse.ArgumentParser(description='Audio Classification Training')

  parser.add_argument('--data', type=str, default='recorded_audio.wav')
  parser.add_argument('--dt', type=float, default=1.0,
                      help='time in seconds to sample audio')
  parser.add_argument('--sr', type=int, default=16000,
                      help='sample rate of clean audio')
  parser.add_argument('--threshold', type=str, default=20,
                      help='threshold magnitude for np.int16 dtype')
  args, _ = parser.parse_known_args()

  convert_to_mono_and_resample(args.data)

  make_clips(args.data)

  # Make predictions for each category using the single WAV file
  gender = make_prediction(["feminine", "masculine"], "models/gender_conv2d_30.h5", args)
  quality = make_prediction(["neutral", "raspy", "smooth"], "models/quality_conv2d_30.h5", args)
  range_ = make_prediction(["alto", "bass", "soprano", "tenor"], "models/range_conv2d_30.h5", args)
  speed = make_prediction(["fast", "normal", "slow"], "models/speed_conv2d_30.h5", args)

  print(f"gender: {gender}, quality: {quality}, range: {range_}, speed: {speed}")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

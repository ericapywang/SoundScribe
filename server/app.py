# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from record_audio import save_wav, convert_to_mp3
from transcribe import transcribe
import sounddevice as sd
from multiple_predict import clear_directory, make_clips, convert_to_mono_and_resample, make_prediction
from keybert import KeyBERT
import requests
import os
import time
from dotenv import load_dotenv
from suno import generate_audio, get_clip_details, download_audio

load_dotenv()  # Load your API token from the .env file

# Set your API URLs
POST_URL = "https://studio-api.suno.ai/api/external/generate/"
GET_URL = "https://studio-api.suno.ai/api/external/clips/?ids="

app = Flask(__name__)
CORS(app)
kw_model = KeyBERT()

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

  for idx, doc in enumerate(docs):
    print(f"Document {idx}: {doc}")
    
    # Use MMR to get diverse topics, with a diversity factor of 0.7 (more diversity)
    keywords = kw_model.extract_keywords(
        doc, 
        keyphrase_ngram_range=(1, 3), 
        stop_words='english', 
        use_mmr=True,       # Use Maximal Marginal Relevance
        diversity=0.7,      # Increase diversity, range is [0-1]
        top_n=3             # Get 3 diverse topics
    )
    
    print("Extracted Diverse Topics:", keywords)
    print("-" * 50)

@app.route('/api/generate', method=['GET'])
def generate(topic, tags):
    # Take user input for the topic and tags
    # topic = input("Enter the topic for the song: ")
    tags = input("Enter tags for the song (e.g., pop, rock, etc.): ")
    
    topics = ["super raspy female funky vocal about New York", "classical opera smooth female vocal about New York"]
    
    for i, topic in enumerate(topics, 1):
        print(f"\nProcessing topic {i}: {topic}")
        
        # Step 1: Generate audio from the topic and tags
        clip_id = generate_audio(topic, tags)
        
        # Step 2: If audio is generated, monitor the status until it's ready
        if clip_id:
            audio_url = get_clip_details(clip_id)
            
            # Step 3: If the audio URL is retrieved, download it as an MP3 file
            if audio_url:
                output_file = f"output_{i}_{topic.replace(' ', '_')}.mp3"
                download_audio(audio_url, output_file)

if __name__ == "__main__":
  app.run(debug=True, port=5000)

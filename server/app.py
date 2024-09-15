# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from record_audio import save_wav, convert_to_mp3
from transcribe import transcribe
import sounddevice as sd
from suno import generate_audio, get_clip_details, download_audio

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
  print('hi')

  return ""

@app.route('/api/generate', methods=['GET'])
def generate():
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
                output_file = f"output.mp3"
                download_audio(audio_url, output_file)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

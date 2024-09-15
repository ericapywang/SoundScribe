import whisper
import torch
import numpy as np
import tqdm
from keybert import KeyBERT
from suno import generate_audio, get_clip_details, download_audio

# Initialize the KeyBERT model
kw_model = KeyBERT()

print("Torch version:", torch.__version__)
print("Whisper model loaded successfully.")

def transcribe():
  # Replace "small" with your desired model size
  device = "cuda" if torch.cuda.is_available() else "cpu"
  model = whisper.load_model("small", device=device)

  # Replace with the path to your audio file
  audio_file = "recorded_audio.mp3"

  result = model.transcribe(audio_file)

  transcribed_text = result["text"]

  print("Transcribed Text:")
  print(transcribed_text)

  for idx, doc in enumerate([transcribed_text]):
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
    tags = "pop"
    
    topics = [f"raspy, tenor range, male funky vocal, normal tempo pop song, about {keywords}"]
    
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

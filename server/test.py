import whisper
import torch
import numpy as np
import tqdm
from keybert import KeyBERT

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

  for idx, doc in enumerate(list(transcribed_text)):
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

transcribe()
import whisper
import torch
import numpy as np
import tqdm

print("Torch version:", torch.__version__)
print("Whisper model loaded successfully.")

def main():
    # Replace "small" with your desired model size
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("small", device=device)

    # Replace with the path to your audio file
    audio_file = "sample-1.mp3"

    result = model.transcribe(audio_file)

    transcribed_text = result["text"]

    print("Transcribed Text:")
    print(transcribed_text)

if __name__ == '__main__':
    main()

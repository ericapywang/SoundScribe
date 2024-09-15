from tensorflow.keras.models import load_model
from clean import downsample_mono, envelope
from kapre.time_frequency import STFT, Magnitude, ApplyFilterbank, MagnitudeToDecibel
from sklearn.preprocessing import LabelEncoder
import numpy as np
from glob import glob
import argparse
import os
from tqdm import tqdm
import soundfile as sf
import librosa
from collections import Counter
import shutil

def clear_directory(directory_path):
    # Check if the directory exists
    if os.path.exists(directory_path):
        # Remove all files and subdirectories within the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Delete the file or symbolic link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Delete the directory and all its contents
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'The directory "{directory_path}" does not exist.')

def make_clips(input_dir, clip_duration=1):
    clear_directory("data")
    basename = os.path.basename(input_dir)
    audio_name = os.path.splitext(basename)[0]
    output_dir = os.path.join("data", audio_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio, sample_rate = sf.read(input_dir)
    total_duration = len(audio) / sample_rate  # in seconds

    clip_samples = clip_duration * sample_rate
    
    for i in range(0, int(total_duration), clip_duration):
        start_sample = i * sample_rate
        end_sample = min((i + clip_duration) * sample_rate, len(audio))
        clip = audio[int(start_sample):int(end_sample)]

        # Rename the file to 0.wav, 1.wav, 2.wav, etc.
        output_filename = f"{i // clip_duration}.wav"
        output_path = os.path.join(output_dir, output_filename)
        sf.write(output_path, clip, sample_rate)
        print(f"Exported {output_filename}")

def convert_to_mono_and_resample(file_path):
    # Load the audio file
    audio_data, sample_rate = librosa.load(file_path, sr=None, mono=False)
    
    # Convert to mono
    audio_mono = librosa.to_mono(audio_data)
    
    # Resample to 16,000 Hz
    audio_resampled = librosa.resample(audio_mono, orig_sr=sample_rate, target_sr=16000)
    
    # Save the new file, replacing the original
    sf.write(file_path, audio_resampled, 16000)
    print(f"Processed {file_path}")

def make_prediction(classes, model_name, args):
    print(model_name)
    
    model = load_model(model_name, custom_objects={'STFT': STFT,
                        'Magnitude': Magnitude,
                        'ApplyFilterbank': ApplyFilterbank,
                        'MagnitudeToDecibel': MagnitudeToDecibel})

    basename = os.path.basename(args.data)
    audio_name = os.path.splitext(basename)[0]
    output_dir = os.path.join("data", audio_name)


    wav_paths = os.listdir(output_dir)
    wav_paths = [os.path.join(output_dir, wav_file) for wav_file in wav_paths]
    wav_paths = sorted([x.replace(os.sep, '/') for x in wav_paths if '.wav' in x])
    
    labels = [os.path.split(x)[0].split('/')[-1] for x in wav_paths]
    le = LabelEncoder()
    y_true = le.fit_transform(labels)

    total = 0
    total_elem = 0

    # Initialize a counter to track occurrences of each class
    class_counter = Counter()

    for z, wav_fn in tqdm(enumerate(wav_paths), total=len(wav_paths)):
        rate, wav = downsample_mono(wav_fn, args.sr)
        mask, env = envelope(wav, rate, threshold=args.threshold)
        clean_wav = wav[mask]
        step = int(args.sr*args.dt)
        batch = []

        for i in range(0, clean_wav.shape[0], step):
            sample = clean_wav[i:i+step]
            sample = sample.reshape(-1, 1)
            if sample.shape[0] < step:
                tmp = np.zeros(shape=(step, 1), dtype=np.float32)
                tmp[:sample.shape[0],:] = sample.flatten().reshape(-1, 1)
                sample = tmp
            batch.append(sample)
        
        X_batch = np.array(batch, dtype=np.float32)
        
        if X_batch.shape[0] == 0:
            continue
        
        # Predict the class probabilities for the batch
        y_pred = model.predict(X_batch)
        
        # Compute the mean across all predictions
        y_mean = np.mean(y_pred, axis=0)
        
        # Get the predicted class
        y_pred_class = np.argmax(y_mean)
        
        # Update the counter with the predicted class
        class_counter[classes[y_pred_class]] += 1

    # Find the most common class prediction
    most_common_class = class_counter.most_common(1)[0][0]

    # Return the most common class as a string
    return most_common_class

# if __name__ == '__main__':

#     parser = argparse.ArgumentParser(description='Audio Classification Training')

#     parser.add_argument('--data', type=str, default='recorded_audio.wav')
#     parser.add_argument('--dt', type=float, default=1.0,
#                         help='time in seconds to sample audio')
#     parser.add_argument('--sr', type=int, default=16000,
#                         help='sample rate of clean audio')
#     parser.add_argument('--threshold', type=str, default=20,
#                         help='threshold magnitude for np.int16 dtype')
#     args, _ = parser.parse_known_args()

#     convert_to_mono_and_resample(args.data)

#     make_clips(args.data)

#     # Make predictions for each category using the single WAV file
#     gender = make_prediction(["feminine", "masculine"], "models/gender_conv2d_30.h5", args)
#     quality = make_prediction(["neutral", "raspy", "smooth"], "models/quality_conv2d_30.h5", args)
#     range_ = make_prediction(["alto", "bass", "soprano", "tenor"], "models/range_conv2d_30.h5", args)
#     speed = make_prediction(["fast", "normal", "slow"], "models/speed_conv2d_30.h5", args)

#     print(f"gender: {gender}, quality: {quality}, range: {range_}, speed: {speed}")

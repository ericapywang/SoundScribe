import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()  # Load your API token from the .env file

# Set your API URLs
POST_URL = "https://studio-api.suno.ai/api/external/generate/"
GET_URL = "https://studio-api.suno.ai/api/external/clips/?ids="

# Function to generate audio from text using Suno API
def generate_audio(topic, tags):
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "affiliate-id": "undefined",
        "authorization": f"Bearer {os.getenv('SUNO_API_KEY')}",
        "content-type": "text/plain;charset=UTF-8",
        "origin": "https://suno.com/",
        "referer": "https://suno.com/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    
    # JSON data with the topic and tags
    data = {
        "topic": topic,
        "tags": tags
    }
    
    # Send POST request to initiate audio generation
    response = requests.post(POST_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        clip_id = response_data.get('id')  # Extract the ID for monitoring status
        if clip_id:
            print(f"Audio generation started. Clip ID: {clip_id}")
            return clip_id
        else:
            print("Clip ID not found in the response.")
    else:
        print(f"Failed to initiate audio generation. Status code: {response.status_code}")
        print(f"Response: {response.text}")
    
    return None

# Function to monitor the status of audio generation and get the clip details
def get_clip_details(clip_id, poll_interval=10, timeout=300):
    headers = {
        "authorization": f"Bearer {os.getenv('SUNO_API_KEY')}"
    }
    
    elapsed_time = 0

    # Poll the API until the audio is ready or timeout is reached
    while elapsed_time < timeout:
        print(f"Checking the status of Clip ID: {clip_id} (Elapsed time: {elapsed_time}s)")
        response = requests.get(f"{GET_URL}{clip_id}", headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data:
                audio_url = response_data[0].get('audio_url')
                if audio_url:
                    print(f"Audio generation completed. Audio URL: {audio_url}")
                    return audio_url
                else:
                    print("Audio URL not found yet. Retrying...")
            else:
                print("Clip data not found in the response.")
        else:
            print(f"Failed to get clip details. Status code: {response.status_code}")
            print(f"Response: {response.text}")
        
        time.sleep(poll_interval)  # Wait before retrying
        elapsed_time += poll_interval
    
    print(f"Timeout reached after {timeout} seconds. Audio generation incomplete.")
    return None

# Function to download the MP3 file from the audio URL
def download_audio(audio_url, output_file="output.mp3"):
    response = requests.get(audio_url)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Audio downloaded successfully and saved as {output_file}")
    else:
        print(f"Failed to download the audio. Status code: {response.status_code}")

# Main function to handle the entire flow
# def main():
    # Take user input for the topic and tags
    # topic = input("Enter the topic for the song: ")
    # tags = input("Enter tags for the song (e.g., pop, rock, etc.): ")
    

    # topics = ["super raspy female funky vocal about New York", "classical opera smooth female vocal about New York"]
    
    # for i, topic in enumerate(topics, 1):
    #     print(f"\nProcessing topic {i}: {topic}")
        
    #     # Step 1: Generate audio from the topic and tags
    #     clip_id = generate_audio(topic, tags)
        
    #     # Step 2: If audio is generated, monitor the status until it's ready
    #     if clip_id:
    #         audio_url = get_clip_details(clip_id)
            
    #         # Step 3: If the audio URL is retrieved, download it as an MP3 file
    #         if audio_url:
    #             output_file = f"output.mp3"
    #             download_audio(audio_url, output_file)
            

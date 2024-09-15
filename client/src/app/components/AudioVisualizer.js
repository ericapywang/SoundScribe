import React, { useState, useEffect } from 'react';
import { LiveAudioVisualizer } from 'react-audio-visualize';

export default function Visualizer() {
  const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);

  useEffect(() => {
    async function setupMediaRecorder() {
      try {
        // Request microphone access
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        
        // Create MediaRecorder instance
        const recorder = new MediaRecorder(stream);
        
        // Set MediaRecorder instance to state
        setMediaRecorder(recorder);
      } catch (error) {
        console.error('Error accessing the microphone', error);
      }
    }

    setupMediaRecorder();
  }, []);

  return (
    <div>
      {mediaRecorder && (
        <LiveAudioVisualizer
          mediaRecorder={mediaRecorder}
          width={200}
          height={75}
        />
      )}
    </div>
  )
};

"use client";

import React, { useState, useEffect } from 'react';
import { Box, Button } from '@mui/material';

const numBars = 10; // Number of bars in the volume meter

export default function Playback() {
  const [levels, setLevels] = useState(Array(numBars).fill(0));

  useEffect(() => {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const analyzer = audioContext.createAnalyser();
    let source = null;

    const updateLevels = () => {
      const bufferLength = analyzer.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);

      analyzer.getByteFrequencyData(dataArray);

      // Process the dataArray to set levels
      const newLevels = Array(numBars).fill(0).map((_, i) => {
        const start = Math.floor((i / numBars) * bufferLength);
        const end = Math.floor(((i + 1) / numBars) * bufferLength);
        const sum = dataArray.slice(start, end).reduce((a, b) => a + b, 0);
        return Math.min((sum / (end - start)) / 2, 100); // Normalize and cap at 100
      });

      setLevels(newLevels);
      requestAnimationFrame(updateLevels);
    };

    const startRecording = async () => {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      source = audioContext.createMediaStreamSource(stream);
      source.connect(analyzer);
      analyzer.fftSize = 256;
      updateLevels();
    };

    startRecording();

    return () => {
      if (source) source.disconnect();
      audioContext.close();
    };
  }, []);

  return (
    <Box
      display='flex'
      flexDirection='column'
      alignItems='center'
      justifyContent='center'
      height='90vh'
      width='100vw'
    >
      <VolumeMeter levels={levels} />
      <Button variant='contained' onClick={() => setLevels(Array(numBars).fill(0))}>
        Reset Levels
      </Button>
    </Box>
  );
};

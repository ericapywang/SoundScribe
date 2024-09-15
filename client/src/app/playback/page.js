"use client";

import React, { useState, useEffect, useRef } from 'react';
import { Box, Button } from '@mui/material';
import Dots from '../components/LoadingDots';
import Navbar from '../components/Navbar';

export default function Playback() {
  const audioRef = useRef(null); // Reference for the audio

  useEffect(() => {
    // Create a new Audio object with the correct path to the MP3 file
    audioRef.current = new Audio('/recorded_audio.mp3');
    
    // Clean up the audio on component unmount
    return () => {
      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current = null;
      }
    };
  }, []);

  // Function to handle the play button click
  const handlePlay = () => {
    audioRef.current.play().catch(err => {
      console.error("Failed to play audio:", err);
    });
  };

  return (
    <div>
      <Navbar />
      <Box
        display='flex'
        flexDirection='column'
        justifyContent='center'
        alignItems='center'
        height='90vh'
        width='100vw'
      >
        <Dots word={"Playing"} />
        <Button
          variant="contained"
          color="primary"
          sx={{ marginTop: '20px' }}
          onClick={handlePlay}
        >
          Play Audio
        </Button>
      </Box>
    </div>
  );
}

"use client";

import React, { useState, useEffect, useRef } from 'react';
import { Box, Button } from '@mui/material';
import Dots from '../components/LoadingDots';
import Navbar from '../components/Navbar';

export default function Playback() {
  const audioRef = useRef(null); // Reference for the audio

  useEffect(() => {
    // Create a new Audio object with the correct path to the MP3 file
    audioRef.current = new Audio('../../../output.mp3');

    // Play the audio automatically when the component mounts
    const playAudio = async () => {
      try {
        await audioRef.current.play();
        console.log("Audio is playing");
      } catch (err) {
        console.error("Failed to play audio automatically:", err);
      }
    };

    playAudio();

    // Clean up the audio on component unmount
    return () => {
      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current = null;
      }
    };
  }, []);

  // Function to handle the play button click (in case manual play is needed)
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
          sx={{
            marginTop: '20px',
            background: 'linear-gradient(90deg, #ff7b72, #a855f7)', // Same gradient as Navbar
            padding: '12px 24px',
            fontSize: '18px',
            borderRadius: '30px',
            color: '#fff',
            '&:hover': {
              background: 'linear-gradient(90deg, #a855f7, #ff7b72)', // Reverse gradient on hover
              opacity: 0.9, // Slight transparency on hover
            },
          }}
          onClick={handlePlay}
        >
          Play Audio
        </Button>
      </Box>
    </div>
  );
}
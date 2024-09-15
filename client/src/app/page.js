'use client';
import React, { useState } from 'react';
import { Button, Box, Stack, Typography } from '@mui/material/';
import MicIcon from '@mui/icons-material/Mic';
import { useRouter } from 'next/navigation';
import Navbar from './components/Navbar';

const config = require('../config.json');

export default function Home() {
  const router = useRouter();
  const [isRecording, setRecording] = useState(false);

  const generate = async () => {
    router.push('/loading');
  };

  const startRecording = async () => {
    setRecording(true);
    await fetch(`http://${config.server_host}:${config.server_port}/api/record`, { method: 'GET' });
    // .then(setRecording(false));
  };

  const keyframes = `@keyframes pulse {
    0% {
      transform: scale(1);
      opacity: 1;
    }
    50% {
      transform: scale(1.1);
      opacity: 0.7;
    }
    100% {
      transform: scale(1);
      opacity: 1;
    }
  }
  @keyframes pulse-shadow {
    0% {
      box-shadow: 0 0 0 15px rgba(168, 85, 247, 0.5); /* Change shadow color to match the gradient */
    }
    50% {
      box-shadow: 0 0 0 25px rgba(168, 85, 247, 0.7);
    }
    100% {
      box-shadow: 0 0 0 15px rgba(168, 85, 247, 0.5);
    }
  }
`;

  return (
    <div>
      <Navbar />
      <Box
        display='flex'
        justifyContent='center'
        alignItems='center'
        height='90vh'
        width='100vw'
      >
        <Stack spacing={5}>
          {/* Main Recording Button */}
          <Button
            sx={{
              background: 'linear-gradient(90deg, #ff7b72, #a855f7)', // Gradient similar to your button palette
              borderRadius: '50%',
              width: 200,
              height: 200,
              minWidth: 0,
              '&:hover': {
                boxShadow: '0 0 0 10px rgba(128, 128, 128, 0.3)', // Hover effect for better UI
              },
              animation: isRecording ? 'pulse-shadow 1s infinite' : 'none',
              boxShadow: isRecording ? '0 0 0 15px rgba(168, 85, 247, 0.5)' : 'none', // Change the shadow to match the palette
            }}
            onClick={startRecording}
          >
            <MicIcon style={{ color: 'white', width: 90, height: 90 }}></MicIcon>
          </Button>

          {/* Generate Button */}
          <Button
            sx={{
              background: 'linear-gradient(90deg, #ff7b72, #a855f7)', // Apply the same gradient here
              width: 200,
              height: 60,
              borderRadius: '30px', // Slight rounding for a modern look
              color: 'white',
              fontWeight: 'bold',
              '&:hover': {
                background: 'linear-gradient(90deg, #ff7b72, #a855f7)', // Keep gradient on hover
                boxShadow: '0 0 10px rgba(168, 85, 247, 0.6)', // Add a soft glow on hover
              },
            }}
            onClick={generate}
          >
            <Typography color='inherit'>Generate</Typography>
          </Button>
        </Stack>
      </Box>
      <style>{keyframes}</style>
    </div>
  );
}

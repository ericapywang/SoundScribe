'use client';
import React, { useState } from 'react';
import {Button, Box, Stack, Typography} from '@mui/material/';
import MicIcon from '@mui/icons-material/Mic';
import { useRouter } from 'next/navigation';
import Navbar from './/components/Navbar';

const config = require('../config.json');

export default function Home() {
  const router = useRouter();
  const [isRecording, setRecording] = useState(false);
  const generate = async () => {
    router.push('/loading');
  }

  const startRecording = async () => {
    setRecording(true);
    await fetch(`http://${config.server_host}:${config.server_port}/api/record`, {method: 'GET'});
      //.then(setRecording(false));
  }

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
      box-shadow: 0 0 0 15px rgba(255, 0, 0, 0.5);
    }
    50% {
      box-shadow: 0 0 0 25px rgba(255, 0, 0, 0.7);
    }
    100% {
      box-shadow: 0 0 0 15px rgba(255, 0, 0, 0.5);
    }
  }
`

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
          <Button sx={{backgroundColor: 'blue',
            borderRadius: '50%',
            width: 200,
            height: 200,
            minWidth: 0,
              '&:hover': {
                boxShadow: '0 0 0 10px gray',
              },
            animation: isRecording ? 'pulse-shadow 1s infinite' : 'none',
            boxShadow: isRecording ? '0 0 0 15px rgba(255, 0, 0, 0.5)' : 'none',
            }}
            onClick={startRecording}>
            <MicIcon style={{color: 'white', width: 90, height: 90}}></MicIcon>
          </Button>
          <Button style={{backgroundColor: 'blue', width: 200, height: 60}} onClick={generate}>
            <Typography color='white'>Generate</Typography>
          </Button>
        </Stack>
      </Box>
      <style>{keyframes}</style>
    </div>
  );
}

'use client';
import React from 'react';
import {Button, Box, Stack} from '@mui/material/';
import MicIcon from '@mui/icons-material/Mic';
import { useRouter } from 'next/navigation';
import Visualizer from './components/AudioVisualizer';

const config = require('../config.json');

export default function Home() {
  const router = useRouter();
  const generate = async () => {
    router.push('/loading');
  }

  const startRecording = async () => {
    await fetch(`http://${config.server_host}:${config.server_port}/api/record`, {method: 'GET'})
  }

  return (
    <div>
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
              }}}
            onClick={startRecording}>
            <MicIcon style={{color: 'white', width: 90, height: 90}}></MicIcon>
          </Button>
          <Visualizer />
          <Button style={{backgroundColor: 'blue', width: 200, height: 60}} onClick={generate}>
            Generate
          </Button>
        </Stack>
      </Box>
    </div>
  );
}

'use client';
import React, { useEffect, useState } from 'react';
import {Box} from '@mui/material'
import LoadingDots from '../components/LoadingDots';
import Navbar from '../components/Navbar';
import { useRouter } from 'next/navigation';

const config = require('../../config.json');

export default function App() {
  const router = useRouter();
  const [ignored, setIgnore] = useState(false);

  useEffect(() => {
    if (!ignored) {
      fetch(`http://${config.server_host}:${config.server_port}/api/transcribe`, { method: 'GET' });
      fetch(`http://${config.server_host}:${config.server_port}/api/predict`, { method: 'GET' });
      setIgnore(true)
    }
  }, []); // Empty dependency array to run this effect once when the component mounts

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
        <LoadingDots word={"Loading"} />
      </Box>
    </div>
  );
};

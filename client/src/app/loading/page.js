'use client';
import React, { useEffect, useState, useRef } from 'react';
import {Box} from '@mui/material'
import LoadingDots from '../components/LoadingDots';
import Navbar from '../components/Navbar';
import { useRouter } from 'next/navigation';

const config = require('../../config.json');

export default function App() {
  const router = useRouter();
  //const [ignored, setIgnore] = useState(false);
  const hasMadeApiCalls = useRef(false); // Ref to track if API calls have been made


  const makeApiCalls = async() => {
    const call1 = fetch(`http://${config.server_host}:${config.server_port}/api/transcribe`, { method: 'GET' });
    const call2 = fetch(`http://${config.server_host}:${config.server_port}/api/data`, { method: 'GET' });

    const [response1, response2] = await Promise.all([call1, call2]);

    if (!response1.ok || !response2.ok) {
      console.error("One or both API calls failed:", response1.status, response2.status);
      return; // Stop further execution if there's an error
    }

    await fetch(`http://${config.server_host}:${config.server_port}/api/generate`, {method: 'GET'});

    router.push('/playback');
  }

  useEffect(() => {
    if (!hasMadeApiCalls.current) {
      hasMadeApiCalls.current = true;
      makeApiCalls();
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

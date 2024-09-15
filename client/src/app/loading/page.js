// App.js
import React from 'react';
import {Box, Stack, Typography} from '@mui/material'
import LoadingDots from '../components/LoadingDots';
import Navbar from '../components/Navbar';

export default function App() {
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

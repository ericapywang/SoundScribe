// App.js
import React from 'react';
import {Box, Stack, Typography} from '@mui/material'
import LoadingDots from '../components/Loading';

export default function App() {
  return (
    <div>
      <Box
        display='flex'
        justifyContent='center'
        alignItems='center'
        height='90vh'
        width='100vw'
      >
        <LoadingDots />
      </Box>
    </div>
  );
};

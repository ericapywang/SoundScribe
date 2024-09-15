import React from 'react';
import { Box, Typography } from '@mui/material';

const dotStyle = {
  width: '15px',
  height: '15px',
  margin: '0 5px',
  backgroundColor: '#333',
  borderRadius: '50%',
  animation: 'bounce 1.4s infinite both',
};

const dotStyle1 = {
  ...dotStyle,
  animationDelay: '0s',
};

const dotStyle2 = {
  ...dotStyle,
  animationDelay: '0.2s',
};

const dotStyle3 = {
  ...dotStyle,
  animationDelay: '0.4s',
};

const keyframes = `
  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
      transform: translateY(0);
    }
    40% {
      transform: translateY(-15px);
    }
    60% {
      transform: translateY(-10px);
    }
  }
`;

export default function Dots({ word }) {
  return (<Box display="flex" gap={2} flexDirection="column" alignItems="center" justifyContent="center" height="100vh">
      <Typography variant="h2" gutterBottom>
        {word}
      </Typography>
      <Box display="flex">
        <Box component="span" sx={dotStyle1} />
        <Box component="span" sx={dotStyle2} />
        <Box component="span" sx={dotStyle3} />
      </Box>
      <style>{keyframes}</style>
  </Box>);
};
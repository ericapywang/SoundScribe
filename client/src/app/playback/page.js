"use client";

import React, { useState, useEffect } from 'react';
import { Box, Button } from '@mui/material';
import Dots from '../components/LoadingDots';
import Navbar from '../components/Navbar';

const config = require('../../config.json');

export default function Playback() {
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
        <Dots word={"Playing"} />
      </Box>
    </div>
  );
};

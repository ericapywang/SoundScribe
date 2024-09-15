import React from 'react';
import { AppBar, Toolbar, Box, Typography, Button } from '@mui/material';

export default function Navbar({ isSignedIn, onSignInClick, onSignOutClick }) {
  return (
    <AppBar
      position="static"
      sx={{
        background: 'linear-gradient(90deg, #ff7b72, #a855f7)', // Gradient similar to the image
        padding: '0 2rem',
        boxShadow: '0px 4px 12px rgba(0, 0, 0, 0.25)', // Soft shadow to match the button depth
        borderRadius: '15px', // Rounded edges for the navbar
        margin: '10px', // Add margin to prevent it from touching the edges of the viewport
      }}
    >
      <Toolbar sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%' }}>
        {/* Left side: Logo or App name */}
        <Typography variant="h6" component="div" sx={{ fontWeight: 'bold', color: '#fff' }}>
          SoundScribe
        </Typography>

        {/* Right side: Conditional Sign In/Out buttons */}
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          {isSignedIn ? (
            <Button
              variant="outlined"
              sx={{ color: '#fff', borderColor: '#fff', marginLeft: 2 }}
              onClick={onSignOutClick}
            >
              Sign Out
            </Button>
          ) : (
            <Button
              variant="outlined"
              sx={{
                background: 'linear-gradient(90deg, #a855f7, #ff7b72)', // Opposite gradient (purple to coral pink)
                padding: '0.5rem 1.5rem', // Padding for the button
                borderRadius: '50px', // Rounded edges for the button
                border: '2px solid white', // White border
                fontWeight: 'bold',
                fontSize: '16px',
                color: '#fff', // White text on the button
                '&:hover': {
                  background: 'linear-gradient(90deg, #a855f7, #ff7b72)', // Keep the opposite gradient on hover
                  opacity: 0.9, // Slight transparency on hover
                },
              }}
              onClick={onSignInClick}
            >
              Sign In
            </Button>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
}

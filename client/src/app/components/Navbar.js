import React from 'react';
import { AppBar, Toolbar, Box } from '@mui/material';
import {
  ClerkProvider,
  SignInButton,
  SignedIn,
  SignedOut,
  UserButton
} from '@clerk/nextjs';

export default function Navbar() {
    return (
      <AppBar position="static" sx={{ width: '100%', backgroundColor: 'blue' }}>
        <Toolbar sx={{ width: '100%', display: 'flex', justifyContent: 'space-between'}} >
          <ClerkProvider>
            <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
              <SignedOut>
                <SignInButton />
              </SignedOut>
              <SignedIn>
                <UserButton />
              </SignedIn>
            </Box>
          </ClerkProvider>
        </Toolbar>
      </AppBar>
    );
};

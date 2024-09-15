// import Image from "next/image";
import {Button, Box, Stack} from '@mui/material/';
import MicIcon from '@mui/icons-material/Mic';

export default function Home() {
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
          <Button style={{backgroundColor: 'blue', borderRadius: '50%', width: 200, height: 200, minWidth: 0}}>
            <MicIcon style={{color: 'white', width: 90, height: 90}}></MicIcon>
          </Button>
          <Button style={{backgroundColor: 'blue', width: 200, height: 60}}>
            Generate
          </Button>
        </Stack>
      </Box>
    </div>
  );
}

// import Image from "next/image";
import {Button} from '@mui/material/';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';

export default function Home() {
  return (
    <div>
      <Button>
        <PlayArrowIcon></PlayArrowIcon>
      </Button>
      <Button>
        Generate
      </Button>
    </div>
  );
}

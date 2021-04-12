# youtube-video-player-with-counters
Python program that plays a YouTube video and allows the user to increment multiple counters. The counters a written to a csv file automatically

## Requirements
- Python 3
- opencv
- VidGear https://abhitronix.github.io/vidgear/latest/

## Usage:
To run, provide the youtube video url as sys arg inclosed in quotes

```
python3 videoCounterTest.py "<YOUTUBE_URL>"
```

## Output:
The output of each counter is saved to a VIDEO_ID.csv

Where each column is:
```
Interval, couter1, counter2, counter3
```

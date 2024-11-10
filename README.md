# spotenstein

## What?

A self-hosted tech stack using Docker/FastAPI/yt-dlp that allows you to press a button on your browser when watching a YouTube video and having that audio be added to your Apple Music (app). 

## Installation and Setup

Create a `.env` file in the project root that looks like:

```
MUSIC_DOWNLOADS_PATH=/Users/<your user name>/Music/Music/Media.localized/Automatically Add to Music.localized
```

Run:

```bash
make start
```

Then, copy the contents of `bookmarklet.js` into a new bookmark in your favorite browser. This works best if you add it to your bookmark bar. 

## Usage

1. Go to some video
2. Click your bookmarklet

There is no step 3. The audio of that video should appear in Apple Music (formerly iTunes). 

## Testing

```bash
curl -k -X POST https://localhost:5566/AddToMusic -H "Content-Type: application/json" -H "Origin: https://youtube.com" -d '{"url": "<some url>"}'
```



## Disclaimer

This was created purely as an exercise in seeing how far I could build something without knowing anything about anything. Don't use this. 

## License 

GPLv3
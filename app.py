import os
import shutil
import uuid

import yt_dlp
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DownloadRequest(BaseModel):
    url: str


@app.post("/AddToMusic")
async def download_video(request: DownloadRequest):
    url = request.url

    # Create a randomly named temp directory for this task
    work_dir = f"/app/scratch/{uuid.uuid4()}"
    os.makedirs(work_dir, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{work_dir}/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        # Run yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download complete.")

        # Move downloaded files to the final downloads directory
        for filename in os.listdir(work_dir):
            shutil.move(os.path.join(work_dir, filename), "/app/downloads/")

        return {"status": "Download completed"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Clean up the temporary directory
        shutil.rmtree(work_dir, ignore_errors=True)


# Ensure necessary directories exist
os.makedirs("/app/scratch", exist_ok=True)
os.makedirs("/app/downloads", exist_ok=True)

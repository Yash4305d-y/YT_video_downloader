import yt_dlp
import tkinter as tk
from tkinter import filedialog
import sys
from urllib.parse import urlparse, parse_qs

def clean_youtube_url(url):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    video_id = query.get("v", [None])[0]
    if not video_id:
        return url
    return f"https://www.youtube.com/watch?v={video_id}"

def download_video(url):
    try:
        root = tk.Tk()
        root.withdraw()
        save_path = filedialog.askdirectory(title="Select Folder to Save Video")
        if not save_path:
            print("❌ Download cancelled — no folder selected.")
            return

        clean_url = clean_youtube_url(url)
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'merge_output_format': 'mp4',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'cachedir': False,
            'progress_hooks': [lambda d: print(f"⬇️  {d['_percent_str']} downloaded", end="\r") if d['status'] == 'downloading' else None],
        }

        print(f"🎬 Downloading: {clean_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([clean_url])

        print(f"\n✅ Download complete!\n📂 Saved in: {save_path}")
    except Exception as e:
        print("❌ Error while downloading:", e)

url = "https://www.youtube.com/watch?v=1lyiQVwSc9U&list=RD1lyiQVwSc9U&start_radio=1"
download_video(url)

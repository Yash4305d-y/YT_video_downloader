import yt_dlp
import tkinter as tk
from tkinter import filedialog
import sys

def download_video(url):
    try:
        root = tk.Tk()
        root.withdraw()
        save_path = filedialog.askdirectory(title="Select Folder to Save Video")

        if not save_path:
            print("❌ Download cancelled — no folder selected.")
            sys.exit()

        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'mp4/best',
            'quiet': False,
        }

        print(f"🎬 Downloading video from: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"✅ Video downloaded successfully!\n📂 Saved in: {save_path}")

    except Exception as e:
        print("❌ Error while downloading:", e)

url = "https://www.youtube.com/watch?v=KAe3CHA4vU8&list=RDKAe3CHA4vU8&start_radio=1"
download_video(url)

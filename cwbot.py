#!/usr/bin/env python3

import os
import subprocess
import shutil
import sys

print("\n                                        Created By PW JARVIS")
print("                                        For assistance, please visit @PWJARVIS on Telegram")
print("                                        ______________________________________________________\n")

# Check for yt-dlp
if not shutil.which("yt-dlp"):
    print("Error: yt-dlp not found. Please ensure yt-dlp is installed and added to your system PATH.")
    print("You can install it via pip: pip install yt-dlp")
    sys.exit(1)

# Check for ffmpeg (required for .m3u8 processing)
if not shutil.which("ffmpeg"):
    print("Error: ffmpeg not found. Please ensure ffmpeg is installed and added to your system PATH.")
    print("You can install it via Chocolatey with: choco install ffmpeg")
    print("Or download from https://ffmpeg.org/download.html and add it to PATH.")
    sys.exit(1)

# Create and navigate to appropriate directory
os.makedirs("PWJarvis", exist_ok=True)
os.chdir("PWJarvis")

batch = "Arjuna NEET 3.0 2025"
os.makedirs(batch, exist_ok=True)
os.chdir(batch)

# Navigate to the target directory (same as original script)
print(":: Subject: Notices")
os.makedirs("Notices/Batch Demo Videos/Lectures", exist_ok=True)
os.chdir("Notices/Batch Demo Videos/Lectures")

# Download parameters
url = "https://stream.pwjarvis.app/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2aWRlb0lkIjoiMTE2MzYxNGYtYTA5YS00YWIzLWFlNmItODJlYmI1ODIzOGUzIiwiZXhwIjoxNzU0NzE5MTkyfQ.RhTJPf3awMA-v-JCCrWmAH5VlH2vFLItiyuPv_jhW8U/hls/720/main.m3u8"
output_file = "unnamed.mp4"

# Check if file already exists
if os.path.exists(output_file):
    print(f"File exists: {output_file} - skipping download")
else:
    print(f"\nStarting download: {output_file}")
    # Run yt-dlp with options for faster .m3u8 downloading
    try:
        subprocess.run([
            "yt-dlp",
            "--no-warnings",
            "--progress",
            "--console-title",
            "-f", "bestvideo+bestaudio/best",  # Select best quality
            "--concurrent-fragments", "8",     # Download up to 8 fragments in parallel
            "-o", output_file,
            url
        ], check=True)
        print(f"Download completed: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: yt-dlp executable not found. Please ensure yt-dlp is installed and in your PATH.")
        print("Install via pip: pip install yt-dlp")
        sys.exit(1)

# Get the full path of the downloaded file
output_path = os.path.abspath(output_file)
print(f"\nDownload completed. File saved in {output_path}")
print("Press Enter to exit.")
input()

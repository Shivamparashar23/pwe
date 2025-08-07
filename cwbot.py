

import os
import subprocess
import shutil
import sys

print("\n                                        Created By PW JARVIS")
print("                                        For assistance, please visit @PWJARVIS on Telegram")
print("                                        ______________________________________________________\n")

# Check for aria2c
if not shutil.which("aria2c"):
    print("Error: aria2c not found. Please ensure aria2c is installed and added to your system PATH.")
    print("Install via Chocolatey: choco install aria2")
    print("Or download from https://aria2.github.io/ and add to PATH.")
    sys.exit(1)

# Check for ffmpeg (required for .m3u8 processing)
if not shutil.which("ffmpeg"):
    print("Error: ffmpeg not found. Please ensure ffmpeg is installed and added to your system PATH.")
    print("Install via Chocolatey: choco install ffmpeg")
    print("Or download from https://ffmpeg.org/download.html and add to PATH.")
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
    # Run aria2c with parallel download options
    try:
        subprocess.run([
            "aria2c",
            url,
            "-o", output_file,
            "-x", "16",  # Maximum 16 connections per server
            "-s", "50",  # Split into 50 segments
            "-k", "1M",  # Minimum split size of 1MB
            "--allow-overwrite=true",
            "--auto-file-renaming=false",
            "--file-allocation=none"  # Faster for large files
        ], check=True)
        print(f"Download completed: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")
        print("The server may not support 50 segments. Try reducing to 20 segments by editing the script.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: aria2c executable not found. Please ensure aria2c is installed and in your PATH.")
        print("Install via Chocolatey: choco install aria2")
        sys.exit(1)

# Get the full path of the downloaded file
output_path = os.path.abspath(output_file)
print(f"\nDownload completed. File saved in {output_path}")
print("Press Enter to exit.")
input()

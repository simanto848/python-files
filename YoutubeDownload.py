"""
Created on Fri Jun  7 21:57:47 2024

@author: Simanto
"""

import os
from pytube import YouTube

DOWNLOAD_PATH = r'A:\Songs'

def show_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'Downloading... {percentage_of_completion:.2f}%')

def download_video(url, quality):
    yt = YouTube(url, on_progress_callback=show_progress)
    video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    
    if quality.lower() == 'high':
        stream = video_streams.desc().first()
    else:
        stream = video_streams.asc().first()
    
    print(f'Downloading {stream.resolution} video...')
    stream.download(output_path=DOWNLOAD_PATH)
    print(f'Video downloaded successfully to {DOWNLOAD_PATH}!')

def download_audio(url):
    yt = YouTube(url, on_progress_callback=show_progress)
    audio_stream = yt.streams.filter(only_audio=True).first()
    
    print(f'Downloading audio...')
    out_file = audio_stream.download(output_path=DOWNLOAD_PATH)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(f'Audio downloaded successfully to {DOWNLOAD_PATH}!')

def main():
    url = input("Enter the YouTube video URL: ")
    choice = input("Do you want to download video or audio? (video(V)/audio(A)): ").strip().lower()

    if choice == 'v':
        quality = input("Choose quality (high/low): ").strip().lower()
        download_video(url, quality)
    elif choice == 'a':
        download_audio(url)
    else:
        print("Invalid choice. Please enter 'video' or 'audio'.")

if __name__ == "__main__":
    main()

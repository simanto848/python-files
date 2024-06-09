"""
Created on Sun Jun  9 11:35:00 2024

@author: Simanto
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from pytube import YouTube
import os

DOWNLOAD_PATH = '/storage/emulated/0/Download'

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

class YouTubeDownloaderApp(App):
    def build(self):
        self.url_input = TextInput(hint_text='Enter the YouTube video URL', multiline=False)
        self.download_type = Spinner(text='Select Download Type', values=('Video', 'Audio'))
        self.quality_spinner = Spinner(text='Select Quality', values=('High', 'Low'))
        self.download_button = Button(text='Download', on_press=self.start_download)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='YouTube Downloader'))
        layout.add_widget(self.url_input)
        layout.add_widget(self.download_type)
        layout.add_widget(self.quality_spinner)
        layout.add_widget(self.download_button)
        
        return layout
    
    def start_download(self, instance):
        url = self.url_input.text
        choice = self.download_type.text.lower()
        if choice == 'video':
            quality = self.quality_spinner.text.lower()
            download_video(url, quality)
        elif choice == 'audio':
            download_audio(url)
        else:
            print("Invalid choice. Please select 'Video' or 'Audio'.")

if __name__ == '__main__':
    YouTubeDownloaderApp().run()

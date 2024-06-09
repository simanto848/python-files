"""
Created on Sun Jun  9 14:30:47 2024

@author: Simanto
"""

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, filedialog
from pytube import YouTube

# Default download path
download_path = r'A:\Songs'

def show_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_var.set(percentage_of_completion)
    progress_label_var.set(f'{percentage_of_completion:.2f}%')
    root.update_idletasks()

def download_video(url, quality):
    yt = YouTube(url, on_progress_callback=show_progress)
    video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    stream = video_streams.filter(res=quality).first()
    
    print(f'Downloading {stream.resolution} video...')
    stream.download(output_path=download_path)
    print(f'Video downloaded successfully to {download_path}!')
    messagebox.showinfo("Success", f"Video downloaded successfully to {download_path}!")

def download_audio(url, quality):
    yt = YouTube(url, on_progress_callback=show_progress)
    audio_stream = yt.streams.filter(only_audio=True, abr=quality).first()
    
    print(f'Downloading audio...')
    out_file = audio_stream.download(output_path=download_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(f'Audio downloaded successfully to {download_path}!')
    messagebox.showinfo("Success", f"Audio downloaded successfully to {download_path}!")

def fetch_qualities():
    url = url_entry.get()
    yt = YouTube(url)
    choice = var.get()
    
    if choice == 'video':
        video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
        qualities = [stream.resolution for stream in video_streams]
    else:
        audio_streams = yt.streams.filter(only_audio=True).order_by('abr')
        qualities = [stream.abr for stream in audio_streams]
    
    quality_var.set('')
    quality_menu['menu'].delete(0, 'end')
    
    for quality in qualities:
        quality_menu['menu'].add_command(label=quality, command=tk._setit(quality_var, quality))

def start_download():
    url = url_entry.get()
    choice = var.get()
    quality = quality_var.get()
    
    progress_var.set(0)
    progress_label_var.set('0%')
    
    if choice == 'video':
        download_video(url, quality)
    elif choice == 'audio':
        download_audio(url, quality)
    else:
        messagebox.showerror("Error", "Invalid choice. Please select 'Video' or 'Audio'.")
    
    url_entry.delete(0, 'end')
    quality_var.set('')


def select_download_location():
    global download_path
    download_path = filedialog.askdirectory(initialdir=download_path)
    if download_path:
        download_path_var.set(download_path)

def on_enter(e):
    download_button_canvas.itemconfig(button_rect, fill="#5E5E5E")

def on_leave(e):
    download_button_canvas.itemconfig(button_rect, fill="#3E3E3E")

root = tk.Tk()
root.title("YouTube Downloader")

# Adding a frame for styling purposes
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Styling
style = ttk.Style()
style.configure("TFrame", background="#2E2E2E")
style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Helvetica", 12))
style.configure("TRadiobutton", background="#2E2E2E", foreground="white", font=("Helvetica", 12))
style.configure("TProgressbar", thickness=20, troughcolor='#2E2E2E', background='#3E3E3E')

# Adding widgets
ttk.Label(mainframe, text="YouTube URL:").grid(row=0, column=0, sticky=tk.W, pady=5)
url_entry = ttk.Entry(mainframe, width=50)
url_entry.grid(row=0, column=1, pady=5)

ttk.Button(mainframe, text="Fetch Qualities", command=fetch_qualities).grid(row=0, column=2, pady=5)

ttk.Label(mainframe, text="Download Type:").grid(row=1, column=0, sticky=tk.W, pady=5)
var = tk.StringVar(value='video')
ttk.Radiobutton(mainframe, text="Video", variable=var, value='video').grid(row=1, column=1, sticky=tk.W, pady=5)
ttk.Radiobutton(mainframe, text="Audio", variable=var, value='audio').grid(row=1, column=2, sticky=tk.W, pady=5)

ttk.Label(mainframe, text="Quality:").grid(row=2, column=0, sticky=tk.W, pady=5)
quality_var = tk.StringVar()
quality_menu = ttk.OptionMenu(mainframe, quality_var, '')
quality_menu.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

ttk.Label(mainframe, text="Download Location:").grid(row=3, column=0, sticky=tk.W, pady=5)
download_path_var = tk.StringVar(value=download_path)
download_path_label = ttk.Label(mainframe, textvariable=download_path_var)
download_path_label.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
browse_button = ttk.Button(mainframe, text="Browse", command=select_download_location)
browse_button.grid(row=3, column=2, sticky=tk.W, pady=5)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(mainframe, variable=progress_var, maximum=100)
progress_bar.grid(row=4, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

progress_label_var = tk.StringVar(value='0%')
progress_label = ttk.Label(mainframe, textvariable=progress_label_var)
progress_label.grid(row=4, column=3, pady=10, padx=5, sticky=tk.W)

# Custom download button
download_button_canvas = tk.Canvas(mainframe, width=100, height=40, bg="#2E2E2E", highlightthickness=0)
button_rect = download_button_canvas.create_rectangle(5, 5, 95, 35, outline="", fill="#3E3E3E", width=2)
button_text = download_button_canvas.create_text(50, 20, text="Download", fill="white", font=("Helvetica", 12))

download_button_canvas.grid(row=5, column=1, columnspan=2, pady=10)
download_button_canvas.bind("<Button-1>", lambda e: start_download())
download_button_canvas.bind("<Enter>", on_enter)
download_button_canvas.bind("<Leave>", on_leave)

# Set the minimum size of the window
root.minsize(600, 300)
root.mainloop()

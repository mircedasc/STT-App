import threading
import itertools
import sys
import time
import re
import tkinter as tk
from tkinter import filedialog
import whisper

def loading_animation(stop_event):
    for frame in itertools.cycle(["|", "/", "-", "\\"]):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\rTranscribing... {frame}")
        sys.stdout.flush()
        time.sleep(0.1)

root = tk.Tk()
root.withdraw()

audio_path = filedialog.askopenfilename(
    title="Select an audio file",
    filetypes=[("Audio files", "*.mp3 *.wav *.m4a *.flac"), ("All files", "*.*")]
)

if not audio_path:
    print("No file selected. Exiting.")
    sys.exit()

stop_event = threading.Event()
thread = threading.Thread(target=loading_animation, args=(stop_event,))
thread.start()

model = whisper.load_model("medium")
result = model.transcribe(audio_path, language="ro")

stop_event.set()
thread.join()
print("\rTranscription complete!       ")

text = result["text"]

sentences = re.split(r'(?<=[.?!])\s+', text.strip())

with open("transcription.txt", "w", encoding="utf-8") as f:
    for sentence in sentences:
        f.write(sentence.strip() + "\n")

print("Transcription saved to transcription.txt")

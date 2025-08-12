import whisper
import re
import threading
import itertools
import sys
import time

def loading_animation(stop_event):
    for frame in itertools.cycle(["|", "/", "-", "\\"]):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\rTranscribing... {frame}")
        sys.stdout.flush()
        time.sleep(0.1)

stop_event = threading.Event()
thread = threading.Thread(target=loading_animation, args=(stop_event,))
thread.start()

model = whisper.load_model("medium")

audio_path = "8 Curiozitaţi Geografice.mp3"

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

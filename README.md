🎙️ Whisper Transcriber (GUI)

A simple desktop application built with Tkinter and OpenAI Whisper that lets you upload an audio file, automatically transcribe it into text, and save the transcription as a .txt file.

---

🚀 Features

Upload audio files (.mp3, .wav, .m4a, .flac) through a friendly interface

Automatic transcription using OpenAI’s Whisper model

Sentence-splitting for better readability

Save transcription as a .txt file anywhere on your computer

Upload and transcribe multiple files in one session

---

🖥️ How to Use

Click Upload Audio File.

Choose your .mp3, .wav, .m4a, or .flac file.

Wait while the transcription runs (status will show Transcribing...  ⏳).

When it’s done, status will turn ✅ Transcription complete!.

Click Save Transcription to choose where to store your .txt file.

You can then upload another file and repeat the process.

---

💾 Download the Release

You can download the latest compiled `.exe` version of Whisper Transcriber from https://github.com/mircedasc/STT-App/releases/tag/release

Reminder: Whisper needs FFmpeg for audio file handling. Scroll down to see how to download

⚠️ If the `.exe` doesn’t work on your system, follow the manual setup steps below.  

---

🔧 Manual Setup & Run (only if `.exe` fails)


1. Clone the repository
```
git clone https://github.com/mircedasc/STT-App.git
cd STT-App
```
2. Create and activate a virtual environment (recommended)
```
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```
```
# Windows 
python -m venv venv
.\venv\Scripts\Activate
```

3. Install dependencies directly
```
pip install torch openai-whisper
```

⚠️ tkinter usually comes with Python.

If it’s missing:

Ubuntu/Debian: 
```
sudo apt install python3-tk
```

Windows/macOS: included with Python installer.

4. Install FFmpeg

Whisper needs FFmpeg for audio file handling:

If it's missing:

Windows: powershell
```
choco install ffmpeg -y
```

macOS (Homebrew):
```
brew install ffmpeg
````

Ubuntu/Debian:
```
sudo apt update
sudo apt install ffmpeg
```
5. Run the app
```
python .venv/transcribe.py
```
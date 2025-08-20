import threading
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import whisper

class TranscriberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whisper Transcriber")
        self.root.geometry("420x220")

        self.label = tk.Label(root, text="Upload an audio file to transcribe", font=("Arial", 12))
        self.label.pack(pady=20)

        self.upload_btn = tk.Button(root, text="Upload Audio File", command=self.upload_file, width=20, height=2)
        self.upload_btn.pack()

        self.status_label = tk.Label(root, text="", fg="blue", font=("Arial", 10))
        self.status_label.pack(pady=10)

        self.save_btn = tk.Button(root, text="Save Transcription", command=self.save_transcription, state="disabled", width=20, height=2)
        self.save_btn.pack()

        self.text = ""

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Select an audio file",
            filetypes=[("Audio files", "*.mp3 *.wav *.m4a *.flac"), ("All files", "*.*")]
        )
        if not file_path:
            return

        self.status_label.config(text="Transcribing...  please wait ⏳")
        self.upload_btn.config(state="disabled")
        self.save_btn.config(state="disabled")
        self.text = ""

        thread = threading.Thread(target=self.transcribe, args=(file_path,))
        thread.start()

    def transcribe(self, file_path):
        try:
            model = whisper.load_model("medium")
            result = model.transcribe(file_path, language="ro")
            text = result["text"]

            sentences = re.split(r'(?<=[.?!])\s+', text.strip())
            self.text = "\n".join(s.strip() for s in sentences)

            # Update UI back on main thread
            self.root.after(0, self.transcription_complete)

        except Exception as e:
            self.root.after(0, lambda: self.status_label.config(text=f"Error: {e}"))

    def transcription_complete(self):
        self.status_label.config(text="✅ Transcription complete!", fg="green")
        self.save_btn.config(state="normal")
        self.upload_btn.config(state="normal")

    def save_transcription(self):
        if not self.text:
            messagebox.showerror("Error", "No transcription available to save.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save transcription as"
        )
        if save_path:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(self.text)
            messagebox.showinfo("Saved", f"Transcription saved to:\n{save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranscriberApp(root)
    root.mainloop()

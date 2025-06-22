from tkinter import Tk, Button, Text, END
import pyaudio
import wave
import threading
import deepgram_api  # Assuming this is the file where Deepgram API functions are defined

class LiveTranscriberUI:
    def __init__(self, master):
        self.master = master
        master.title("Live Transcriber")

        self.text_area = Text(master, wrap='word', height=20, width=50)
        self.text_area.pack(pady=10)

        self.record_button = Button(master, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack(pady=10)

        self.is_recording = False
        self.audio_thread = None

    def toggle_recording(self):
        if self.is_recording:
            self.stop_recording()
        else:
            self.start_recording()

    def start_recording(self):
        self.is_recording = True
        self.record_button.config(text="Stop Recording")
        self.audio_thread = threading.Thread(target=self.record_audio)
        self.audio_thread.start()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.config(text="Start Recording")

    def record_audio(self):
        # Initialize PyAudio
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

        frames = []

        while self.is_recording:
            data = stream.read(1024)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the audio data to a temporary file or send it directly to Deepgram API
        self.transcribe_audio(frames)

    def transcribe_audio(self, frames):
        # Convert frames to the appropriate format and send to Deepgram API
        audio_data = b''.join(frames)
        transcription = deepgram_api.transcribe_audio(audio_data)  # Assuming this function exists
        self.display_transcription(transcription)

    def display_transcription(self, transcription):
        self.text_area.insert(END, transcription + '\n')
        self.text_area.see(END)

if __name__ == "__main__":
    root = Tk()
    live_transcriber = LiveTranscriberUI(root)
    root.mainloop()
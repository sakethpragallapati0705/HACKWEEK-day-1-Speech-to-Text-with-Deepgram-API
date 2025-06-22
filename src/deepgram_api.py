from deepgram import Deepgram
import asyncio
import os
import sounddevice as sd
import wave

DEEPGRAM_API_KEY = '1f921f39c383090bedad159fc7b314ed4d4055c8'  # Replace with your actual API key
deepgram_client = Deepgram(DEEPGRAM_API_KEY)

audio_file_path = 'c:/Users/sasrb/Desktop/Hack Week/Day-1/deepgram-live-transcriber/audio_file.wav'

def record_audio(duration=5, sample_rate=44100):
    """Record audio and save it to a file."""
    print("Recording audio...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    with wave.open(audio_file_path, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())
    print(f"Audio recorded and saved to {audio_file_path}")

async def transcribe_audio():
    try:
        if not os.path.exists(audio_file_path):
            print(f"Error: File not found at {audio_file_path}")
            return "Error: File not found."
        else:
            with open(audio_file_path, 'rb') as audio:
                # Pass the audio file as a dictionary with 'buffer' and 'mimetype'
                response = await deepgram_client.transcription.prerecorded(
                    {'buffer': audio, 'mimetype': 'audio/wav'},
                    {'punctuate': True, 'language': 'en'}
                )
                # Extract the transcription text from the response
                transcription = response['results']['channels'][0]['alternatives'][0]['transcript']
                return transcription
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

def start_recording():
    record_audio()  # Record audio before transcription
    transcription = asyncio.run(transcribe_audio())
    return transcription

def stop_recording():
    print("Recording stopped.")
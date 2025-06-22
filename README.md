# Deepgram Live Transcriber

This project is a live voice transcription tool that utilizes the Deepgram API to convert spoken language into text in real-time. It features a user-friendly interface with a button to start/stop recording and a text area to display the transcribed text.

## Project Structure

```
deepgram-live-transcriber
├── src
│   ├── app.py              # Main entry point of the application
│   ├── deepgram_api.py     # Functions to interact with the Deepgram API
│   ├── src
|   │   ├── templates
|   │   │   └── index.html      # Main UI for the application
|   │   ├── static
|   │   │   └── styles.css 
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

## Setup Instructions

### 1. Clone the repository:
```bash
git clone <repository-url>
cd deepgram-live-transcriber
```

### 2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set up the Deepgram API key:
- Obtain your Deepgram API key from the [Deepgram website](https://www.deepgram.com/).
- Set your API key either in the environment variables or directly in the `deepgram_api.py` file.

## Usage Guidelines

### 1. Run the application:
```bash
python src/app.py
```

### 2. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

- Click the **"Start Recording"** button to begin capturing audio.
- Click the button again to stop recording.
- The transcribed text will appear in the text area as you speak.

## Overview of Functionality

- **Real-time Transcription**: The application listens to voice input and transcribes it live using the Deepgram API.
- **User Interface**: A simple UI allows users to control the recording and view the transcribed text.
- **Audio Handling**: The application manages audio input and processes it for transcription.

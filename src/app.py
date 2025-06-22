from flask import Flask, render_template, request
import threading
import deepgram_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_recording', methods=['POST'])
def start_recording():
    transcription = deepgram_api.start_recording()
    return {'transcription': transcription}, 200

@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    deepgram_api.stop_recording()
    return 'Recording stopped', 200

if __name__ == '__main__':
    app.run(debug=True)
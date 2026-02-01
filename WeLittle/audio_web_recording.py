from flask import Flask, request, jsonify
from pydub import AudioSegment
import os
import uuid
from datetime import datetime
from flask import send_from_directory

app = Flask(__name__)

UPLOAD_DIR = "WeLittle/recordings"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/upload", methods=["POST"])
def upload_audio():
    file = request.files["audio"]
    
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    temp_filename = f"{timestamp}_audio.webm"

    temp_path = os.path.join(UPLOAD_DIR, temp_filename)
    file.save(temp_path)

    mp3_filename = temp_filename.replace(".webm", ".mp3")
    mp3_path = os.path.join(UPLOAD_DIR, mp3_filename)

    audio = AudioSegment.from_file(temp_path)
    audio.export(mp3_path, format="mp3")

    os.remove(temp_path)

    return jsonify({
        "message": "Audio saved successfully",
        "file": mp3_filename
    })

if __name__ == "__main__":
    app.run(debug=True)

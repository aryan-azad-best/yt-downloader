from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    format = request.args.get('format', 'mp4')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Run yt-dlp to fetch video/audio
    command = f'yt-dlp -f best -o "downloads/%(title)s.%(ext)s" {url}'
    subprocess.run(command, shell=True)

    # Get the downloaded file name
    files = os.listdir("downloads")
    if not files:
        return jsonify({"error": "Download failed"}), 500

    return jsonify({"message": "Download complete", "file": files[0]})

if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    app.run(host='0.0.0.0', port=8080)

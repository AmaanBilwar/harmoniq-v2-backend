import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Directory to save images
UPLOAD_DIR = "captured_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/api/captured_images', methods=['GET','POST'])
def save_images():
    if 'image' not in request.files:
        print("No image file found")
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    print(f"Received file: {image_file.filename}")

    if image_file:
        filename = secure_filename(image_file.filename)
        file_path = os.path.join(UPLOAD_DIR, filename)
        image_file.save(file_path)
        print(f"Image saved at: {file_path}")
        return jsonify({'message': 'Image saved successfully', 'path': file_path}), 200
    else:
        print("Invalid file")
        return jsonify({'error': 'Invalid file'}), 400


if __name__ == '__main__':
    app.run(debug=True)

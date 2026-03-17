import os
from datetime import datetime

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'uploads', 'food_images')
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_image(uploaded_file):
    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ext = os.path.splitext(uploaded_file.name)[1]
    if not ext:
        ext = '.jpg'
    
    filename = f"image_{timestamp}{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    return filename, file_path

def get_image_path(filename):
    return os.path.join(UPLOAD_DIR, filename)

def calculate_calories_burned(steps):
    return steps * 0.04

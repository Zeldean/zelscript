"""Image converter - converts all non-PNG images to PNG format"""
import os
from PIL import Image

def convert_to_png(directory):
    """Convert all non-PNG images in directory to PNG format"""
    for (root, _, files) in os.walk(directory):
        for file in files:
            if not file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                name, _ = os.path.splitext(file_path)
                
                with Image.open(file_path) as img:
                    img.save(f"{name}.png", "PNG")
                
                os.remove(file_path)
                print(f"Converted {file} to PNG")
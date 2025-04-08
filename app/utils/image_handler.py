import os
from fastapi import UploadFile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = BASE_DIR / "static" / "images"

def save_image(image: UploadFile) -> str:
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    image_path = IMAGE_DIR / image.filename
    with open(image_path, "wb") as buffer:
        buffer.write(image.file.read())
    return str(image_path)

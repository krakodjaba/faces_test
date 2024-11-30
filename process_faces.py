import cv2
from retinaface import RetinaFace
import requests
import os

# URL вашего API
API_URL = "http://your-api.com/upload"

def process_frame(image_path):
    """Обрабатывает один кадр, вырезает лицо и отправляет его на API."""
    img = cv2.imread(image_path)
    if img is None:
        print(f"Не удалось загрузить изображение: {image_path}")
        return

    faces = RetinaFace.detect_faces(img)
    if not faces:
        print(f"Лицо не найдено в кадре: {image_path}")
        return

    for face_id, face in faces.items():
        x1, y1, x2, y2 = face["facial_area"]
        cropped_face = img[y1:y2, x1:x2]
        _, buffer = cv2.imencode('.jpg', cropped_face)

        # Отправка на API
        response = requests.post(API_URL, files={"file": ("face.jpg", buffer.tobytes())})
        if response.status_code == 200:
            print(f"Успешно отправлено: {image_path}")
        else:
            print(f"Ошибка отправки: {response.status_code}, {response.text}")

def main():
    """Обрабатывает все кадры из папки frames."""
    frames_dir = "frames"
    for frame_file in os.listdir(frames_dir):
        if frame_file.endswith(".png"):
            process_frame(os.path.join(frames_dir, frame_file))

if __name__ == "__main__":
    main()

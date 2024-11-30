#!/bin/bash
# Удаление старых файлов
rm -rf frames/
mkdir frames

echo "Запуск записи и обработки..."
while true; do
    # Запись экрана в файл
    screenrecord --output-format=h264 screen.mp4 &
    PID=$!

    # Запись экрана на 10 секунд
    sleep 10
    kill $PID

    # Извлечение кадров
    ffmpeg -i screen.mp4 -vf fps=5 frames/frame_%03d.png

    # Обработка кадров
    python process_faces.py
done

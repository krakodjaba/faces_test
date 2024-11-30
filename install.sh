#!/bin/bash
# Обновление и установка пакетов
pkg update && pkg upgrade -y
pkg install python ffmpeg git -y

# Установка Python-зависимостей
pip install --upgrade pip
pip install -r requirements.txt

echo "Установка завершена!"

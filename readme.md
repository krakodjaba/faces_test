### README.md

```markdown
# FaceDetect-ScreenCapture

Этот репозиторий — **тестовый проект** для экспериментов с технологией обнаружения лиц на кадрах экрана смартфона. Целью является создание простого рабочего прототипа, который:
- Записывает экран устройства.
- Разделяет видео на кадры.
- Обнаруживает лица с помощью библиотеки **RetinaFace**.
- Вырезает найденные лица и отправляет их на указанный API.

## ⚠️ Этические принципы

Мы настоятельно призываем использовать данный проект **исключительно в рамках этики**:
- Для собственных исследований и обучения.
- Для тестирования технологий в контролируемых условиях.
- **Не использовать для слежки, нарушения конфиденциальности или других незаконных действий.**

Если вы планируете использовать этот проект в реальных сценариях, убедитесь, что это не нарушает прав других людей.

## 📋 Возможности

- **Минимальная настройка**: достаточно Android-устройства и Termux.
- **Модульная структура**: скрипты легко адаптируются под ваши задачи.
- **Реальное применение**: демонстрация работы детектора лиц RetinaFace.

## 🔧 Установка

1. Установите [Termux](https://f-droid.org/packages/com.termux/).
2. Клонируйте репозиторий:
   ```bash
   git clone <ссылка-на-репозиторий>
   cd <имя-репозитория>
   ```
3. Запустите установку:
   ```bash
   bash install.sh
   ```

## 🚀 Запуск

1. Убедитесь, что ваш API готов принимать данные.
2. Запустите основной скрипт:
   ```bash
   bash start.sh
   ```

## 💡 Как это работает?

1. **Запись экрана**: `screenrecord` записывает видео экрана устройства.
2. **Извлечение кадров**: `ffmpeg` разделяет видео на отдельные кадры.
3. **Обработка кадров**: `process_faces.py` обнаруживает лица на кадрах, вырезает их и отправляет на указанный API.

## 🛠 Требования

- Android-устройство с установленным Termux.
- Подключение к интернету (для отправки данных на API).
- Знание основ Python (опционально, для модификации скриптов).

## 🤝 Присоединяйтесь

Этот проект — экспериментальный и открыт для идей и предложений. Если вы хотите помочь в разработке, тестировании или даже финансово поддержать проект, напишите мне:
- Email: [op@santgbots.ru]

Ваша помощь может быть любой: от предоставления идей до доработки существующего функционала.

## ⚠️ Отказ от ответственности

Автор не несёт ответственности за любое неэтичное использование данного кода. Ваша ответственность — использовать проект в рамках законов и норм.

---

Спасибо за интерес к проекту! Вместе мы можем сделать технологии лучше и доступнее. 🌟
```
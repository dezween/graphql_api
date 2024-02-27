# Используем официальный образ Python 3.10
FROM python:3.10

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы из текущей директории в рабочую директорию
COPY . .

# Запускаем приложение
CMD ["python", "app.py"]
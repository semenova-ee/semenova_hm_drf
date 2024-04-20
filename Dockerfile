# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY ./reqs.txt /app/

# Устанавливаем зависимости
RUN pip install -r /app/reqs.txt

# Копируем код приложения в контейнер
COPY . .

# Команда для запуска приложения при старте контейнера
# CMD ["python", "manage.py", "runserver"]
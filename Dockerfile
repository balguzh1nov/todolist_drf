# Используем базовый образ Python
FROM python:3.8

# Устанавливаем переменную окружения для отключения режима вывода
ENV PYTHONUNBUFFERED 1

# Создаём директорию для приложения
RUN mkdir /todolist

# Устанавливаем рабочую директорию
WORKDIR /todolist

# Копируем зависимости в контейнер
COPY requirements.txt /todolist/

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все остальные файлы в контейнер
COPY . /todolist/

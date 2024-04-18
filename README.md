

# Настройка DRF в Docker
## Клонировать проект:

https://github.com/semenova-ee/semenova_hm_drf

- Перейти в папку проекта, установить виртуальное окружение 

`python -m venv venv`

- Установить зависимости 

`pip install -r reqs.txt`

- Подготовить миграции 

`python manage.py makemigrations`

Провести миграции 

`python manage.py migrate`

## Сборка без yaml файла
- Сборка докер образа:

`docker build -t my-python-app . `

- Запуск контейнера:

`docker run my-python-app`


- Сборка с yaml файлом
- 
## Cоздание образа из Dockerfile:

`docker-compose build`

- с запуском контейнера:

`docker-compose up --build`

- с запуском конктейнера в фоновом режиме:

`docker-compose up -d --build`

- Запуск контейнера:

`docker-compose up`


# Запуск проекта:
Запуск Jango проекта через Run - "название проекта" или командой `python manage.py runserver`
Описание:
Реализовать платформу для онлайн-обучения. Разработка LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.


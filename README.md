# Запуск проекта:
Запуск Jango проекта через Run - "название проекта" или командой `python manage.py runserver`

# Настройка DRF в Docker
## Клонировать проект:

https://github.com/semenova-ee/semenova_hm_drf

## Сборка без yaml файла
### Сборка докер образа:

`docker build -t my-python-app . `

### Запуск контейнера:

`docker run my-python-app`


### Сборка с yaml файлом
Cоздание образа из Dockerfile:

`docker-compose build`

с запуском контейнера:

`docker-compose up --build`

с запуском конктейнера в фоновом режиме:

`docker-compose up -d --build`

Запуск контейнера:

`docker-compose up`

Описание:
Реализовать платформу для онлайн-обучения. Разработка LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.


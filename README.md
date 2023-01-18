# Сервис управления рассылками

## Задача
Необходимо разработать сервис управления рассылками API администрирования и получения статистики.

## Требования к запуску

* docker
* docker-compose

## Запуск
1. Войти в папку проекта
1. Выполнить команду: **docker network create fabrique-net**
1. Перед запуском необходимо в папке env создать файл: **.env.private** (В папке env есть пример этого файла)
1. Выполнить команду: **docker-compose up --build** (При первом запуске api может лежать, так как бд не успевает инициализироваться. Рекомандуется перезапустить docker-compose up)
1. Необходимо сделать миграции:
    1. Войти в docker контейнер api: **docker exec -it api /bin/bash**
    1. Выполнить команду: **python manage.py makemigrations**
    1. Выполнить команду: **python manage.py migrate**
    1. (Опционально) Создать суперпользователя:
        1. Выполнить команду: **python manage.py createsuperuser**
        2. Ввести логин, почту и пароль 

## Основные задачи
* Обращение к api происходит по 8080 порту;
* Документация: http://localhost:8080/docs;
* Реализованы методы создания рассылки, просмотр созданных и получение статистики;
* Реализован сервис отправки уведомлений на внешнее API;
* Рассылка сообщений происходит с помощью celery. Данная технология позволяет отложить задачу или перезапустить ее при ошибке.

## Дополнительные задачи
* Подготовил docker-compose ;
* Документация SwaggerUI: http://localhost:8080/docs ; 
* Реализована обработка ошибок и откладывание запросов при неуспехе для последующей повторной отправки;
* Ежедневная рассылка статистики администраторам;
* Тесты:
    * Клиенты
* OAuth2: Вход через Яндекс;
* ...

## Инструменты
* Django rest framework - api
* PosgreSQL - основная база данных
* Celery - менеджер задач
* Redis - база данных 'ключ-значение' и брокер очередей для celery 
* Flower - мониторинг задач celery
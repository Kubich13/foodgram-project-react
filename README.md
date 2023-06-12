# Project Foodgram

## Технологии
- Python;
- Django-Rest-Framework;
- PPostgreSQL;
- PGunicorn;
- PDocker/Docker-compose;
- PNginx;
- PYandex.Cloud;
- PGithub Actions.

## Описание
Foodgram - социальная сеть для публикации рецептов. В Foodgram реализована функция подписки на авторов, добавление рецептов в избранное, ингредиенты в список покупок, скачивать список покупок.

## Доступ

Проект запущен на сервере и доступен по адресам:

- http://84.252.129.147
- Админ - http://84.252.129.147/admin/
- API - http://84.252.129.147/api/

Админы доступы:

Логин: admin
email: test@test.com
password: STu-rqA-425-HJU

## Для локального запуска

### 1. Загрузите репозиторий

### 2. Создайте .env файлы. Например:

- DB_ENGINE=<...>
- DB_NAME=<...>
- POSTGRES_USER=<...>
- POSTGRES_PASSWORD=<...>
- DB_HOST=<...>
- DB_PORT=<...>
- SECRET_KEY=<...>

### 3. Выполните команды

- docker-compose up -d --build
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py createsuperuser
- docker-compose exec web python manage.py collectstatic --no-input
- docker-compose exec web python manage.py csv_import
- перейдите http://localhost/


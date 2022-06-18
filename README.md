# Тестовое задание

Ссылка на гугл таблицу https://docs.google.com/spreadsheets/d/1JDWsC5gtyiffa0EOanWts3-hcCAn_9j6Pfu8lU74SDw/edit#gid=0

## Как запустить

Скачайте код ```git clone ``` и перейдите в каталог

Создайте файл переменного окружения .env со следующим содержимым:
```
DJANGO_SECRET_KEY=секретный ключ Django
TELEGRAM_CHAT_ID=чтобы узнать напишите телеграм боту @userinfobot
TELEGRAM_BOT_TOKEN=токен созданного бота через @BotFather
```
Далле создайте образ и запустите контейнер
```sh
docker compose up
```
Выполните команды
```sh
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```
Чтобы загрузить данные и уведомить об окончании срока поставки
```commandline
docker compose exec web python manage.py load_data
docker compose exec web python manage.py notify
```
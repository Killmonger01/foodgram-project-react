# praktikum_new_diplom
# Описание
Foodgram это сайт для размещение своих рецептов
# Стек
Python - Django, JavaScript - React
# Автор
Ризабеков Алишер
# Как запустить локально
- создайте файл .env в корне проекта и укажите там следующие переменные
'''
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
SECRET_KEY = ...
'''
- Перейдите в папку infra/ и пропешите следующию команду
'''
docker compose up --build
'''
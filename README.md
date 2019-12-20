# flask-restful-api-example
Python Restful API example using Flask and PostgreSQL


Quickstart
----------

#### Clone repository
```shell
git clone https://github.com/DenerRodrigues/flask-restful-api-example.git
```

#### Install requirements.txt

```shell
pip install -r requirements.txt
```

#### Set environment variables in the `.env` file at project root

Variable                | Description                                   | Example
------------------------|---------------------------------------------- |--------------------------------------------------------
FLASK_DEBUG             | Flask Debug                                   | True
FLASK_ENV               | Flask Environment                             | Development
FLASK_SECRET_KEY        | Secret Key of Flask Application               | 506da44b-3587-47af-93c5-856b29890111
BASE_URL                | Base URL of Flask Application                 | http://127.0.0.1:5000
SQLALCHEMY_DATABASE_URI | Database URL                                  | postgres://`user`:`password`@`host`:`5432`/`database`
AUTH_TOKEN_EXPIRATION   | Authentication Token Expiration Minutes Time  | 600

#### Run Migrations
```shell
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

#### Run Application
```shell
python run.py
```

#### Run Tests
```shell
python manage.py tests
```

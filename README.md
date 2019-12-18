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

Variable                | Description         | Example
------------------------|---------------------|--------------------
FLASK_DEBUG             | Flask Debug         | True
FLASK_ENV               | Flask Environment   | Development
SQLALCHEMY_DATABASE_URI | Database URL        | postgres://`user`:`password`@`host`:`5432`/`database`

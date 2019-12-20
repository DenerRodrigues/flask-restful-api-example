from flask import redirect

from api.app import app


@app.route('/')
def index():
    description = 'Python Restful API example using Flask and PostgreSQL!'
    swagger = '<a target="_blank" href="http://127.0.0.1:5000/docs/spec.html#!/spec">Swagger</a>'
    github = '<a target="_blank" href="https://github.com/DenerRodrigues/flask-restful-api-example">GitHub</a>'
    return '{}<br><ul><li>{}</li><li>{}</li></ul>'.format(description, swagger, github)


@app.route('/docs')
def docs():
    return redirect('/docs/spec.html#!/spec')

from flask import redirect

from api.app import app


@app.route('/')
def index():
    description = 'Python Restful API example using Flask and PostgreSQL!'
    swagger = '<a target="_blank" href="{}/docs/spec.html#!/spec">Swagger</a>'.format(app.config.get('BASE_URL'))
    github = '<a target="_blank" href="https://github.com/DenerRodrigues/flask-restful-api-example">GitHub</a>'
    return '{}<br><ul><li>{}</li><li>{}</li></ul>'.format(description, swagger, github)


@app.route('/docs')
def docs():
    return redirect('/docs/spec.html#!/spec')

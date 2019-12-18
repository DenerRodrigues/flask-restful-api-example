from api.app import app


@app.route('/')
def index():
    return 'Python Restful API example using Flask and PostgreSQL!'

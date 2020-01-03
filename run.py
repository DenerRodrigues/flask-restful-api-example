from api.app import app

if __name__ == '__main__':
    app.run(host=app.config.get('BASE_URL'))

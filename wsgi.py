#wsgi bridge for gunicorn to flask
from app import app
if __name__ == "__main__":
    app.run()
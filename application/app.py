from flask import Flask
from application.bp.homepage.homepage import homepage

def init_app():
    app = Flask(__name__)
    app.register_blueprint(homepage)
    return app

# expose a module-level app for local use (flask --app application.app:app run)
app = init_app()

if __name__ == "__main__":
    app.run(debug=True)

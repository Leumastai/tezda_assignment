from os import environ
from flask import Flask
from views import recc_blueprint

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(recc_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host = '0.0.0.0', port=environ.get("PORT", 5100), threaded=True)
    # uwsgi --socket 0.0.0.0:5000 --protocol=http -w app.app:create_app()
    

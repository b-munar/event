from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.controllers.ping_controller import Ping
from src.controllers.event_controller import EventController, PartnerController, SportmenController

def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(Ping, '/event/ping')
    api.add_resource(EventController, '/event')
    api.add_resource(SportmenController, '/event/sportmen')
    api.add_resource(PartnerController, '/event/partner')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=80, host='0.0.0.0')
else:
    gunicorn_app = create_app()
from flask_restful import Resource
from flask import request

from src.schemas.sportmen_schema import SportmenDeserializeSchema, SportmenSerializeSchema
from src.database.session import Session
from src.models.event_model import EventModel, Sportmen
from src.schemas.event_schema import EventDeserializeSchema, EventSerializeSchema
from src.utils.authorization import authorization

class EventController(Resource):
    method_decorators = [authorization]
    def get(self, **kwargs):
        event_schema = EventSerializeSchema()

        session = Session()
        query = session.query(EventModel).filter()
        session.close()
        
        events = [event_schema.dump(event) for event in query]
        return {"events":events}, 200

class PartnerController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        event_create_schema = EventDeserializeSchema()
        
        errors = event_create_schema.validate(request_json)
        if errors:
            return "", 400
        
        event_create_dump = event_create_schema.dump(request_json)
        event_create_dump["user"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_event = EventModel(**event_create_dump)
        session.add(new_event)
        session.commit()

        event_created_schema = EventSerializeSchema()
        event_created_dump = event_created_schema.dump(new_event)
        return event_created_dump, 201
    
    def get(self, **kwargs):
        event_schema = EventSerializeSchema()

        session = Session()
        query = session.query(EventModel).filter(EventModel.user==kwargs["user"]["id"])
        session.close()
        
        events = [event_schema.dump(event) for event in query]
        return {"events":events}, 200

class SportmenController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        sportmen_create_schema = SportmenDeserializeSchema()
        
        errors = sportmen_create_schema.validate(request_json)
        if errors:
            print(errors)
            return "", 400
        
        event_create_dump = sportmen_create_schema.dump(request_json)
        event_create_dump["sportmen"] = kwargs["user"]["id"]

        session = Session()
        new_event = Sportmen(**event_create_dump)
        session.add(new_event)
        session.commit()

        event_created_schema = SportmenSerializeSchema()
        event_created_dump = event_created_schema.dump(new_event)
        return event_created_dump, 201

    def get(self, **kwargs):
        sportmen_schema = SportmenSerializeSchema()

        session = Session()
        query = session.query(Sportmen).filter(Sportmen.sportmen==kwargs["user"]["id"]).all()

        session.close()
        
        events = [sportmen_schema.dump(event)  for event in query]
        return {"events": events}, 200
        
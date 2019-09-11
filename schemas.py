from marshmallow_sqlalchemy import ModelSchema
from models import Houses

class HouseSchema(ModelSchema):
    class Meta:
        model = Houses
# src/models/NluModel.py
from . import db
import datetime, json
from marshmallow import fields, Schema


class NluModel(db.Model):

    __tablename__ = 'nlu'

    id = db.Column("id", db.Integer, primary_key=True)
    type = db.Column("nlu_type", db.String(100), nullable=False)
    name = db.Column("nlu_name", db.String(100), nullable=False)
    value = db.Column("value", db.String(1000), nullable=False)

    def __init__(self, data):
        self.type = data.get('type')
        self.name = data.get('name')
        self.value = json.dumps(data.get('value'))\
            .replace("[", "{")\
            .replace("]", "}")


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_nlu():
        return NluModel.query.all()

    @staticmethod
    def get_one_nlu(id):
        return NluModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


# add this new class
class NluSchema(Schema):

  id = fields.Int(dump_only=True, )
  type = fields.Str(required=True)
  name = fields.Str(required=True)
  value = fields.List(fields.String(), required=True)

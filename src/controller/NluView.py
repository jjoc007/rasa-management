# /src/controller/UserView

import pystache

from flask import request, json, Response, Blueprint
from ..model.NluModel import NluModel, NluSchema
from ..files import commons as cm
from ..utils import nlu_utils as ut


nlu_api = Blueprint('nlu', __name__)
nlu_schema = NluSchema()


@nlu_api.route('/', methods=['POST'])
def create():

    req_data = request.get_json()
    data, error = nlu_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    # check if user already exist in the db
    """
    user_in_db = NluModel.get_user_by_email(data.get('email'))
    if user_in_db:
        message = {'error': 'User already exist, please supply another email address'}
        return custom_response(message, 400)
    """

    nlu = NluModel(data)
    nlu.save()

    ser_data = nlu_schema.dump(nlu).data

    return custom_response({'nlu': ser_data}, 201)


@nlu_api.route('/build', methods=['POST'])
def build():
    # construye los archivos nlu
    print("construir archivos")

    items = NluModel.get_all_nlu()

    for item in items:

        nlu_item = {
            "type": item.type,
            "name": item.name,
            "value": item.value
        }

        renderer = pystache.Renderer()

        path_name = ut.get_nlu_path(nlu_item["type"], +nlu_item["name"])
        rendered_text = renderer.render_path('src/templates/nlu-template.txt', nlu_item)

        cm.save_file(path_name, rendered_text)

    return custom_response({'response': 'success'}, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
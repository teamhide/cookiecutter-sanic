from sanic import Blueprint
from sanic.request import Request
from sanic.response import json

bp = Blueprint('{{cookiecutter.package_name}}_v1', url_prefix='/api/v1/{{cookiecutter.package_name}}')


@bp.route('/', methods=['GET'])
async def home(request: Request) -> json:
    return json(body={'hello': 'world'})

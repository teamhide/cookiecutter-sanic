from sanic import Sanic
from sanic_openapi import swagger_blueprint
from sentry_sdk import init

from apps.{{cookiecutter.package_name}}.views.v1 import bp as {{cookiecutter.package_name}}


def init_listeners(app: Sanic, config):
    @app.listener('before_server_start')
    async def init_db(app, loop):
        pass

    @app.listener('after_server_stop')
    async def close_db(app, loop):
        pass

    @app.middleware('request')
    async def print_on_request(request):
        pass

    @app.middleware('response')
    async def close_session(request, response):
        pass


def init_blueprints(app: Sanic, config):
    app.blueprint({{cookiecutter.package_name}})

    if config.env != 'production':
        app.blueprint(swagger_blueprint)


def init_middlewares(app: Sanic, config):
    pass


def init_exception_handlers(app: Sanic, config):
    if config.env == 'production':
        init(config.sentry_addr)


def create_app(config):
    app = Sanic(__name__)

    init_listeners(app=app, config=config)
    init_blueprints(app=app, config=config)
    init_middlewares(app=app, config=config)
    init_exception_handlers(app=app, config=config)

    return app

import os
from sanic import Sanic
from apps import create_app
from core.configs import get_config


if __name__ == '__main__':
    config = get_config()
    app: Sanic = create_app(config=config)
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=False if config.env == 'production' else True,
        workers=os.cpu_count() if config.env == 'production' else 1
    )

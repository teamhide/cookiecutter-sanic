from datetime import datetime, timedelta

import jwt
from sanic.request import Request

from core.configs import get_config
from core.exceptions import CustomException


class TokenHelper:
    @classmethod
    def extract_from_request(cls, request: Request):
        try:
            return request.headers.get('Authorization').split('Bearer ')[1]
        except (IndexError, AttributeError):
            raise CustomException(message='token header error', code=400)

    @classmethod
    def decode(cls, token: str) -> dict:
        try:
            return jwt.decode(
                token,
                get_config().jwt_secret_key,
                algorithms=[get_config().jwt_algorithm],
            )
        except jwt.exceptions.DecodeError:
            raise CustomException(message='token decode error', code=400)
        except jwt.exceptions.InvalidTokenError:
            raise CustomException(message='invalid token', code=400)

    @classmethod
    def encode(cls, payload: dict, expire_period: int = 3600):
        return jwt.encode(
            payload={
                **payload,
                'exp': datetime.utcnow() + timedelta(seconds=expire_period),
            },
            key=get_config().jwt_secret_key,
            algorithm=get_config().jwt_algorithm,
        )

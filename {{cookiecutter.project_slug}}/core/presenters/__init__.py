import abc
from typing import Any

from sanic.response import json

from core.responses import ResponseObject


class Presenter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    async def transform(self, response: ResponseObject) -> json:
        pass

    async def _process_body(
        self,
        response: ResponseObject,
        serializer: Any = None,
        many: bool = None,
    ) -> dict:
        result = {'body': {'data': None, 'meta': None}, 'status': 200}

        if response.meta:
            result['body']['meta'] = response.meta

        if not response:
            result['body'] = {'status': False}
            result['status'] = 500
            return result

        if response.code:
            result['body'] = {'errors': response.data}
            result['status'] = response.code
            return result

        if serializer:
            result['body']['data'] = serializer().dump(
                response.data,
                many=many,
            )
            return result

        result['body'] = {'status': True}
        return result

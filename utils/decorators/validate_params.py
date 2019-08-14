from cerberus import Validator
from django.http import JsonResponse

from utils.helpers.cerberus_errors import CustomError

import json


def validate_params(schema):
    def decorator(function):
        def wrap(request, *args, **kwargs):
            if request.method == 'POST':
                data = json.loads(request.body)
            elif request.method == 'GET':
                data = request.GET.dict()
            else:
                return JsonResponse({"message": "Invalid Method"}, status=405)
            v = Validator(schema, error_handler=CustomError,
                          allow_unknown=True)
            result = v.validate(data)

            if result:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse(v.errors, status=400)

        return wrap

    return decorator

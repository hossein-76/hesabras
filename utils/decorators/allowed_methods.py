import json
from django.http import JsonResponse


def allowed_methods(request_method_list):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.method not in request_method_list:
                res = {'message':'Invalid method'}
                return JsonResponse(res,status=405)
            else:
                return func(request, *args, **kwargs)

        return wrapper

    return decorator

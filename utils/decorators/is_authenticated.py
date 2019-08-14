import base64
import datetime
import json

from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.conf import settings

# from account.models import User, Token


def is_authenticated(func):
    def wrapper(request, *args, **kwargs):
        res = {'message': "You are not authenticated"}

        if request.user.is_authenticated:
                # if not request.user.deleted:
            return func(request, *args, **kwargs)

        # if 'HTTP_AUTHORIZATION' in request.META:
        # 	try:
        # 		type, token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
        # 	except:
        # 		return JsonResponse(res, status=401)
        # 	if type.lower() == 'basic':
        # 		payload = base64.b64decode(token).decode()
        # 		username, password = payload.split(':', 1)
        # 		if username == settings.HTTP_AUTHORIZATION['username'] and password == settings.HTTP_AUTHORIZATION[
        # 			'password']:
        # 			return func(request, *args, **kwargs)
        # 	if type.lower() == 'token':
        # 		try:
        # 		    user = User.objects.get(key=token, deleted=False)
        # 		    # if user.expired:
        # 		    #     raise Exception
        # 		    # else:
        # 		    request.user = user
        # 		except:
        # 		    res = {'message': 'Token has been expired'}
        # 		    return JsonResponse(res, status=401)
        # 		return func(request, *args, **kwargs)

        return JsonResponse(res, status=401)

    return wrapper

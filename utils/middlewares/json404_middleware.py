from django.http import JsonResponse


class JSON404Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print('sssssssssssss', request.path_info)
        if response.status_code == 404 and 'application/json' not in response[
            'content-type'] and 'api' in request.path_info:
            data = {'detail': '{0} not found'.format(request.path)}
            response = JsonResponse(data, status=404)
        return response

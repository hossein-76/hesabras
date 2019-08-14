from budget.models import OutCome, OutComeCategory
from utils.decorator import allowed_method, is_authenticated, validate_params
import json
import datetime
from django.http import JsonResponse
SCHEMA = {
    'amount': {'type': 'integer', 'coerce': int, 'required': True},
    'title': {'type': 'string', 'required': True},
    'description': {'type': 'string', 'required': False},
    'used_at': {'type': 'string', 'required': False},
    'category': {'type': 'string', 'required': False},
}


@is_authenticated
@allowed_method(['POST'])
@validate_params(SCHEMA)
def add_outcome(request):
    user = request.user
    data = json.loads(request.body)
    amount = data.get('amount')
    title = data.get('title')
    description = data.get('description')
    used_at = data.get('used_at')
    category = data.get('category')
    category, _ = OutComeCategory.objects.get_or_create(title=category)
    used_at = datetime.datetime.strptime(used_at, "%d/%m/%Y").date()
    OutCome.objects.create(title=title, amount=amount, used_at=used_at,
                           description=description, category=category)

    return JsonResponse(data={"message": "ok"}, status=200)

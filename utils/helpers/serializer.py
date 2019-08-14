from django.db.models import QuerySet
from django.forms import model_to_dict

from .validate_fields import validate_fields as fields_validator
from .expand_fields import expand_fields as fields_expander


def parse_query(string, ff):
    try:
        field = string.replace(ff, '', 1)
        if field == '':
            return None
        elif str(field).startswith('__'):
            return field.replace('__', '', 1)
    except:
        return None


def parse_fields(fields):
    if type(fields) != list:
        raise Exception('type is not correct')
    data = {}
    for f in fields:
        field = f.split('__')[0]
        if data.get(field):
            h = parse_query(f, field)
            if h:
                data[field].append(h)
            else:
                data[field] = h
        else:
            h = parse_query(f, field)
            if h:
                data[field] = [h]
            else:
                data[field] = None
    return data


def serializer(objects, fields=None, valid_fields=[]):
    if not objects:
        return []

    is_queryset = True
    if not isinstance(objects, QuerySet) and type(objects) is not list:
        objects = [objects]
        is_queryset = False

    if not fields:
        fields = [i.name for i in objects[0]._meta.get_fields() if
                  not i.auto_created and not str(i).lower() == 'password']
    fields = parse_fields(fields)
    fields, extra_fields = fields_validator(objects[0], fields, valid_fields=valid_fields)
    data = []
    for i in objects:
        obj = model_to_dict(i, fields=fields)
        if extra_fields:
            obj = fields_expander(obj, i, extra_fields, valid_fields=valid_fields)
        data.append(obj)

    return data if is_queryset else data[0]

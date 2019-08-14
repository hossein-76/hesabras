import datetime

from . import serializer


def expand_fields(data, obj, extra_fields, valid_fields=[]):
    if type(extra_fields) == dict:
        for field in extra_fields.keys():
            if field in ['password', 'key']:
                continue
            # print(field)
            try:
                obj._meta.get_field(field)
            except:
                try:
                    my_json = getattr(obj, 'get_clear_' + field)()
                    data[field] = my_json
                except:
                    data[field] = None
                continue
            if field in valid_fields:
                try:
                    my_json = getattr(obj, 'get_clear_' + field)()
                    data[field] = my_json
                    # print('fiiiiiiiiiield', field)
                except:
                    data[field] = None

            elif obj._meta.get_field(field).get_internal_type().lower() == 'datetimefield':
                data[field] = datetime.datetime.strftime(getattr(obj, field), '%Y-%m-%dT%H:%M:%S') if getattr(obj,
                                                                                                              field) else None
            elif obj._meta.get_field(field).get_internal_type().lower() == 'datefield':
                data[field] = datetime.datetime.strftime(getattr(obj, field),
                                                         '%Y/%m/%d')
            elif obj._meta.get_field(field).get_internal_type().lower() == 'foreignkey':
                id = getattr(obj, field)
                data[field] = serializer.serializer(id,
                                                    fields=extra_fields[field], valid_fields=valid_fields)
            elif obj._meta.get_field(field).get_internal_type().lower() == 'manytomanyfield':
                ids = getattr(obj, field).all()
                data[field] = []
                for id in ids:
                    data[field].append(serializer.serializer(id,
                                                             fields=extra_fields[field], valid_fields=valid_fields))
            elif obj._meta.get_field(field).get_internal_type().lower() in ['imagefield', 'filefield']:
                id = getattr(obj, field)
                if id:
                    id = id.url
                else:
                    id = None
                data[field] = id
            else:
                try:
                    my_json = getattr(obj, 'get_clear_' + field)()
                    data[field] = my_json
                except:
                    data[field] = None
    else:
        for field in extra_fields:
            try:
                obj._meta.get_field(field)

            except:
                try:
                    my_json = getattr(obj, 'get_clear_' + field)()
                    data[field] = my_json
                except:
                    data[field] = None
                continue
            if field in valid_fields:
                try:
                    my_json = getattr(obj, 'get_clear_' + field)()
                    data[field] = my_json
                except:
                    data[field] = None
            elif obj._meta.get_field(field).get_internal_type().lower() == 'datetimefield':
                data[field] = datetime.datetime.strftime(
                    getattr(obj, field), '%Y-%m-%dT%H:%M:%S')
            elif obj._meta.get_field(field).get_internal_type().lower() == 'datefield':
                data[field] = datetime.datetime.strftime(
                    getattr(obj, field), '%Y-%m-%d')
            elif obj._meta.get_field(field).get_internal_type().lower() == 'foreignkey':
                id = getattr(obj, field)
                data[field] = serializer.serializer(
                    id, valid_fields=valid_fields)
            elif obj._meta.get_field(field).get_internal_type().lower() == 'manytomanyfield':
                ids = getattr(obj, field).all()
                data[field] = []
                for id in ids:
                    data[field].append(serializer.serializer(
                        id), valid_fields=valid_fields)
            elif obj._meta.get_field(field).get_internal_type().lower() in ['imagefield', 'filefield']:
                id = getattr(obj, field)
                if id:
                    id = id.url
                else:
                    id = None
                data[field] = id
            else:
                try:
                    my_json = getattr(obj, 'get_clear_' + field)()
                    data[field] = my_json
                except:
                    data[field] = None
    return data

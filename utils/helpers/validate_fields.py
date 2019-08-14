class NotValidFieldError(Exception):
    pass


def validate_fields(object, fields, valid_fields=[]):
    if type(fields) == dict:
        extra_fields = {}
        for field in fields.keys():
            if field in valid_fields:  # or getattr(object, 'get_clear_' + field):
                extra_fields[field] = fields[field]
                continue
            try:
                object._meta.get_field(field)
                _type = object._meta.get_field(field).get_internal_type()
                # print(_type)
            except:
                # print(valid_fields)
                raise NotValidFieldError('not valid field '+field)
            if _type.lower() in ['foreignkey', 'manytomany', 'manytomanyfield', 'datetimefield', 'datefields',
                                 'filefield', 'jsonfield', 'imagefield']:
                extra_fields[field] = fields[field]
                continue
        fields = [x for x in fields if x not in extra_fields.keys()]
    else:
        extra_fields = []
        for field in fields:
            if field in valid_fields:  # or getattr(object, 'get_clear_' + field):
                extra_fields.append(field)
                continue
            try:
                object._meta.get_field(field)
                _type = object._meta.get_field(field).get_internal_type()
            except:
                raise NotValidFieldError('not valid field '+field)
            if _type.lower() in ['foreignkey', 'manytomany', 'manytomanyfield', 'datetimefield', 'datefields',
                                 'filefield', 'jsonfield', 'imagefield']:
                extra_fields.append(field)
                continue
        fields = [x for x in fields if x not in extra_fields]
    return fields, extra_fields

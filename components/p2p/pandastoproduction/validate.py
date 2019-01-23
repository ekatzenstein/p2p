

def validate_type(name, obj, expected_type, nullable=True):
    if obj is None and nullable == True:
        return
    if not isinstance(obj, expected_type):
        raise TypeError(f'Error with {name}: Expected type {expected_type} but received type {type(obj)}.')


def validate_type_list(name, obj, expected_type):
    validate_type(name, obj, list)
    for i, item in enumerate(obj):
        validate_type(f'{name}[{i}]', item, expected_type)

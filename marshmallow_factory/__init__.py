from marshmallow import Schema
from marshmallow.schema import SchemaMeta
from marshmallow.fields import Nested


__version__ = '0.1.0'


def schema(_schema_dict=None, **kwargs):
    _schema_dict = dict(_schema_dict or kwargs)  # create copy for changes

    for key, value in _schema_dict.items():
        if isinstance(value, dict):
            _schema_dict[key] = nested_schema(value)

    # Passing empty string prevents class from getting added
    # to marshmallow's class registry, thus saving memory
    return SchemaMeta(str(''), (Schema,), _schema_dict)


schema_factory = schema  # alternative import name


def nested_schema(*args, **kwargs):
    return Nested(schema(*args, **kwargs))

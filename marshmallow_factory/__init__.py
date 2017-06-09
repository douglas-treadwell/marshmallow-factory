from marshmallow import Schema
from marshmallow.schema import SchemaMeta


def schema(_schema_dict=None, **kwargs):
    return SchemaMeta('AnonymousSchema', (Schema,), _schema_dict or kwargs)


schema_factory = schema  # alternative import name

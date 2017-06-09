from marshmallow import Schema
from marshmallow.schema import SchemaMeta


def schema(schema_dict):
    return SchemaMeta('AnonymousSchema', (Schema,), schema_dict)


schema_factory = schema  # alternative import name

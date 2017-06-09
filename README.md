Marshmallow Factory
===================


Inspired by [Voluptuous](https://github.com/alecthomas/voluptuous).

It's sometimes inconvenient to define named 
[Marshmallow](https://github.com/marshmallow-code/marshmallow)
Schemas, especially when those schemas are deeply nested.

Example:

```
class InnerSchema(Schema):
    inner_bool = Boolean()


class MiddleSchema(Schema):
    middle_int = Integer()
    middle_nested = Nested(InnerSchema)


class OuterSchema(Schema):
    outer_str = String()
    outer_nested = Nested(MiddleSchema)


schema_instance = OuterSchema(input_)
schema_instance.validate()
```

So, this library provides a convenient syntax for defining
deeply nested Schemas.

```
OuterSchema = schema({
    'outer_str': String(),
    'outer_nested': Nested(schema({
        'middle_int': Integer(),
        'middle_nested': Nested(schema({
            'inner_bool': Boolean()
        }))
    }))
})

schema_instance = OuterSchema(input_)
schema_instance.validate()
```


Support For Meta Options
------------------------

Meta options are supported using the following syntax:

```
class Meta:
    strict = True  # or your other options

my_schema = schema({
    'Meta': Meta,
    'str': String()
})
```


Alternative Syntax
------------------

Schema factory arguments can also be supplied as keyword
arguments rather than a dictionary.

```
my_schema = schema(Meta=Meta, str=String())
```

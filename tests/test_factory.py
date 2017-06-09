from unittest import TestCase
from marshmallow.fields import String, Integer, Boolean, Nested
from marshmallow.exceptions import ValidationError
from marshmallow_factory import schema


class TestFactory(TestCase):
    def test_simple_factory(self):
        my_schema = schema({
            'str': String()
        })

        input_ = {
            'str': 'str'
        }

        data, errors = my_schema().load(input_)

        self.assertEqual(len(errors), 0)

        my_schema().validate(input_)

    def test_meta_options(self):
        class Meta:
            strict = True

        my_schema = schema({
            'Meta': Meta,
            'str': String()
        })

        input_ = {
            'str': 1
        }

        # verify that class Meta: strict = True took effect
        with self.assertRaises(ValidationError):
            data, errors = my_schema().load(input_)

    def test_factory_with_kwargs(self):
        class Meta:
            strict = True

        my_schema = schema(Meta=Meta, str=String())

        input_ = {
            'str': 1
        }

        # verify that class Meta: strict = True took effect
        with self.assertRaises(ValidationError):
            data, errors = my_schema().load(input_)

        input_ = {
            'str': 'str'
        }

        data, errors = my_schema().load(input_)

        self.assertEqual(len(errors), 0)  # for good measure

    def test_nested_factory(self):
        my_schema = schema({
            'str': String(),
            'nested': Nested(schema({
                'nested_str': String()
            }))
        })

        input_ = {
            'str': 'str',
            'nested': {
                'nested_str': 'str'
            }
        }

        data, errors = my_schema().load(input_)

        self.assertEqual(len(errors), 0)

        my_schema().validate({'x': 1})

    def test_readme_example(self):
        OuterSchema = schema({
            'outer_str': String(),
            'outer_nested': Nested(schema({
                'middle_int': Integer(),
                'middle_nested': Nested(schema({
                    'inner_bool': Boolean()
                }))
            }))
        })

        input_ = {
            'outer_str': 'str',
            'outer_nested': {
                'middle_int': 1,
                'middle_nested': {
                    'inner_bool': True
                }
            }
        }

        data, errors = OuterSchema().load(input_)

        self.assertEqual(len(errors), 0)

        OuterSchema().validate(input_)

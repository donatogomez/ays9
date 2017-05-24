"""
Auto-generated class for Actor
"""
from .Action import Action

from . import client_support


class Actor(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(actions, name, role, schema):
        """
        :type actions: list[Action]
        :type name: str
        :type role: str
        :type schema: str
        :rtype: Actor
        """

        return Actor(
            actions=actions,
            name=name,
            role=role,
            schema=schema,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Actor'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'actions'
        val = data.get(property_name)
        if val is not None:
            datatypes = [Action]
            try:
                self.actions = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'name'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.name = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'role'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.role = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'schema'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.schema = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

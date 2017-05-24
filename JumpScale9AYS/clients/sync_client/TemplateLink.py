"""
Auto-generated class for TemplateLink
"""

from . import client_support


class TemplateLink(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(argname, auto, max, min, role):
        """
        :type argname: str
        :type auto: bool
        :type max: int
        :type min: int
        :type role: str
        :rtype: TemplateLink
        """

        return TemplateLink(
            argname=argname,
            auto=auto,
            max=max,
            min=min,
            role=role,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'TemplateLink'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'argname'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.argname = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'auto'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.auto = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'max'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.max = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'min'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.min = client_support.val_factory(val, datatypes)
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

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

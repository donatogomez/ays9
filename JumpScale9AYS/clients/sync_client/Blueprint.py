"""
Auto-generated class for Blueprint
"""

from . import client_support


class Blueprint(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(archived, content, hash, name, path):
        """
        :type archived: bool
        :type content: str
        :type hash: str
        :type name: str
        :type path: str
        :rtype: Blueprint
        """

        return Blueprint(
            archived=archived,
            content=content,
            hash=hash,
            name=name,
            path=path,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Blueprint'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'archived'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.archived = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'content'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.content = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'hash'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.hash = client_support.val_factory(val, datatypes)
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

        property_name = 'path'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.path = client_support.val_factory(val, datatypes)
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

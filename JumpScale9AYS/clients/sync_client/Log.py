"""
Auto-generated class for Log
"""

from . import client_support


class Log(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(category, epoch, level, log, tags):
        """
        :type category: str
        :type epoch: int
        :type level: int
        :type log: str
        :type tags: str
        :rtype: Log
        """

        return Log(
            category=category,
            epoch=epoch,
            level=level,
            log=log,
            tags=tags,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Log'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'category'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.category = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'epoch'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.epoch = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'level'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.level = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'log'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.log = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'tags'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.tags = client_support.val_factory(val, datatypes)
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

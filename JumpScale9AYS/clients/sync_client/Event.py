"""
Auto-generated class for Event
"""

from . import client_support


class Event(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(actions, channel, command, tags):
        """
        :type actions: list[str]
        :type channel: str
        :type command: str
        :type tags: list[str]
        :rtype: Event
        """

        return Event(
            actions=actions,
            channel=channel,
            command=command,
            tags=tags,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Event'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'actions'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.actions = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'channel'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.channel = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'command'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.command = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'tags'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.tags = client_support.list_factory(val, datatypes)
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

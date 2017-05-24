"""
Auto-generated class for Job
"""
from .Log import Log

from . import client_support


class Job(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(action_name, actor, key, logs, service_key, service_name, state):
        """
        :type action_name: str
        :type actor: str
        :type key: str
        :type logs: list[Log]
        :type service_key: str
        :type service_name: str
        :type state: str
        :rtype: Job
        """

        return Job(
            action_name=action_name,
            actor=actor,
            key=key,
            logs=logs,
            service_key=service_key,
            service_name=service_name,
            state=state,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Job'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'action_name'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.action_name = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'actor'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.actor = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'key'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.key = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'logs'
        val = data.get(property_name)
        if val is not None:
            datatypes = [Log]
            try:
                self.logs = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'service_key'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.service_key = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'service_name'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.service_name = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'state'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.state = client_support.val_factory(val, datatypes)
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

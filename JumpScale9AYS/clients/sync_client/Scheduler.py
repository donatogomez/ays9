"""
Auto-generated class for Scheduler
"""
from .EnumSchedulerStatus import EnumSchedulerStatus

from . import client_support


class Scheduler(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(queueSize, status):
        """
        :type queueSize: int
        :type status: EnumSchedulerStatus
        :rtype: Scheduler
        """

        return Scheduler(
            queueSize=queueSize,
            status=status,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Scheduler'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'queueSize'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.queueSize = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'status'
        val = data.get(property_name)
        if val is not None:
            datatypes = [EnumSchedulerStatus]
            try:
                self.status = client_support.val_factory(val, datatypes)
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

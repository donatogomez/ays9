"""
Auto-generated class for TemplateRecurringAction
"""

from . import client_support


class TemplateRecurringAction(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(action, log, period):
        """
        :type action: str
        :type log: bool
        :type period: str
        :rtype: TemplateRecurringAction
        """

        return TemplateRecurringAction(
            action=action,
            log=log,
            period=period,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'TemplateRecurringAction'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'action'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.action = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'log'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.log = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'period'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.period = client_support.val_factory(val, datatypes)
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

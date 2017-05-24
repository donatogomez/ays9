"""
Auto-generated class for TemplateConfig
"""
from .TemplateLink import TemplateLink
from .TemplateRecurringAction import TemplateRecurringAction

from . import client_support


class TemplateConfig(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(links, recurring):
        """
        :type links: list[TemplateLink]
        :type recurring: list[TemplateRecurringAction]
        :rtype: TemplateConfig
        """

        return TemplateConfig(
            links=links,
            recurring=recurring,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'TemplateConfig'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'links'
        val = data.get(property_name)
        if val is not None:
            datatypes = [TemplateLink]
            try:
                self.links = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'recurring'
        val = data.get(property_name)
        if val is not None:
            datatypes = [TemplateRecurringAction]
            try:
                self.recurring = client_support.list_factory(val, datatypes)
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

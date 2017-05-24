"""
Auto-generated class for Service
"""
from .Action import Action
from .Event import Event
from .ServicePointer import ServicePointer

from . import client_support


class Service(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(actions, children, consumers, data, events, key, name, parent, path, producers, repository, role, state):
        """
        :type actions: list[Action]
        :type children: list[ServicePointer]
        :type consumers: list[ServicePointer]
        :type data: dict
        :type events: list[Event]
        :type key: str
        :type name: str
        :type parent: ServicePointer
        :type path: str
        :type producers: list[ServicePointer]
        :type repository: str
        :type role: str
        :type state: str
        :rtype: Service
        """

        return Service(
            actions=actions,
            children=children,
            consumers=consumers,
            data=data,
            events=events,
            key=key,
            name=name,
            parent=parent,
            path=path,
            producers=producers,
            repository=repository,
            role=role,
            state=state,
        )

    def __init__(self, json=None, **kwargs):
        if not json and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Service'
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

        property_name = 'children'
        val = data.get(property_name)
        if val is not None:
            datatypes = [ServicePointer]
            try:
                self.children = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'consumers'
        val = data.get(property_name)
        if val is not None:
            datatypes = [ServicePointer]
            try:
                self.consumers = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'data'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.data = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'events'
        val = data.get(property_name)
        if val is not None:
            datatypes = [Event]
            try:
                self.events = client_support.list_factory(val, datatypes)
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

        property_name = 'parent'
        val = data.get(property_name)
        if val is not None:
            datatypes = [ServicePointer]
            try:
                self.parent = client_support.val_factory(val, datatypes)
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

        property_name = 'producers'
        val = data.get(property_name)
        if val is not None:
            datatypes = [ServicePointer]
            try:
                self.producers = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'repository'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.repository = client_support.val_factory(val, datatypes)
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

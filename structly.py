from collections import OrderedDict

from inspect import Parameter, Signature


def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)


class Desciptor:
    """instance is the instance being manipulated
       e.g. Stock instance
    """
    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class StructureMeta(type):

    # def __prepare__(cls, names,bases):
    #     return OrderedDict()

    def __new__(cls, name, bases, cls_dict):
        # fields = [
        #     key for key, val in cls_dict.items() if isinstance(val, Desciptor)
        # ]
        # for name in fields:
        #     clsdict[name].name = name

        cls_obj = super().__new__(cls, name, bases, dict(cls_dict))
        sig = make_signature(cls_obj._fields)
        setattr(cls_obj, '__signature__', sig)
        return cls_obj


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({args})'


#Desciptor protocal


class Stock(Structure):

    name = Desciptor('name')  # Redfines .shares
    shares = Desciptor('shares')
    price = Desciptor('price')

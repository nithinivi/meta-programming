from structly import Structure, Desciptor

#type checking

class Typed(Desciptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError(f'Expected {self.ty}')
        super().__set__(instance, value)

class Integer(Typed):
    ty=int

class Float(Typed):
    ty=float

class String(Typed):
    ty=str

# value checking

class Postive(Desciptor):
    """this is a mixin class
    """
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f'Must be >= 0')
        super().__set__(instance, value)

#order matter a lot in here

class PostiveInteger(Integer, Postive):
    pass

class PostiveFloat(Float, Postive):
    pass


class Stock(Structure):
    _fields = ['name','shares','price']
    name = String('name') # Redfines .shares
    shares = PostiveInteger('shares')
    price = PostiveFloat('price')

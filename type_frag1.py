from structly import Structure , Desciptor
from typed_struct import Typed, String , PostiveFloat , PostiveInteger



class Size(Desciptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)


    def __set__(self, instance ,value):
        if len(value) > self.maxlen:
            raise ValueError(f'value larger than maxlen {self.maxlen}')
        super().__set__(instance, value )


class SizedString(String, Size):
    pass

class Stock(Structure):
    _fields = ['name','shares','price']
    name = SizedString('name', maxlen=10) # Redfines .shares
    shares = PostiveInteger('shares')
    price = PostiveFloat('price')

class Structure:
    _fields = []

    def __init__(self, *args):
        #self.__class__._fields
        for name, val in zip(self.__class__._fields, args):
            setattr(self, name, val)


class Stock1:
    def __init__(self, name, shares, prices):
        "docstring"
        self.name = name
        self.shares = shares
        self.price = price


class Stock(Structure):
    ## how to access class variable through instance
    _fields = ['name', 'shares', 'price']

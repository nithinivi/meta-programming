from inspect import Parameter , Signature


fields = ['name', 'shares', 'price']
parms = [ Parameter(fname, Parameter.POSITIONAL_OR_KEYWORD)
          for fname in fields]

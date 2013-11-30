from inspect import ismethod

class Record(dict):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def to_dict(self):
        return self
        
class SlotsRecord(object):
    __slots__ = ()

    def __init__(self, **kw):
        for k, v in kw.iteritems():
            setattr(self, k, v)

    def to_dict(self):
        d = {}

        for name in dir(self):
            if name.startswith('__'):
                continue

            attr = getattr(self, name)

            if ismethod(attr):
                continue

            d[name] = attr

        return d

    def __repr__(self):
        return repr(self.to_dict())

    __str__ = __repr__


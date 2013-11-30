"""
Different implementations of a record that can be used with record based
read/write components like those that read/write from/to DB, CVS files etc.

All implementations must meet the following requirements:
  - has a constructor that takes keyword arguments (**kw)
  - implement method to_dict()
  - provide access to attributes through __getattr__, __setattr__
"""

from inspect import ismethod

class Record(dict):
    """
    Basic imlementation based on built-in dictionary that adds access to keys
    using attribute syntax.
    """

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def to_dict(self):
        return self


class SlotsRecord(object):
    """
    More efficient implementation than Record but requires to define all the
    attributes using __slots__. It allows to avoid duplication of keys in every
    record thus improve performance and memory footprint, but only suitable for
    implementations that have "static" record structure.
    """

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


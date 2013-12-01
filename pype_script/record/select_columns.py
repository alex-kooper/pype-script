"""
Create a new record with specified subset of attributes from a Record

It is supposed to be used in a pipline like this:

    pipeline_element | select_columns('a', 'b', 'c') | pipeline_element
"""

from pype_script.record.records import Record
from pype_script import pmap

class ColumnsSelector(object):
    """
    A callable object that selects attributes specified in *args
    """
    def __init__(self, *args):
        self.__args = args

    def __call__(self, record):
        """Build a new record with attributes defined by *args"""
        new_record = Record()

        for name in self.__args:
            new_record.setattr(name, record.getattr(name))

        return new_record

def select_columns(*args):
    return pmap(ColumnsSelector(*args))


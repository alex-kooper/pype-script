"""
Select specified subset of columns from a Record

It is supposed to be used in a pipline like that:

    pipeline_element | select_columns('a', 'b', 'c') | pipeline_element
"""

from pype_script.record.records import Record
from pype_script import pmap

class ColumnSelector(object):
    """
    A callable object that selects columns specified in *args
    """
    def __init__(self, *args):
        self.__args = args

    def __call__(self, record):
        new_record = Record()

        for attr in self.__args:
            new_record.setattr(attr, record.getattr(attr))

        return new_record

def select_columns(*args):
    return pmap(ColumnSelector(*args))


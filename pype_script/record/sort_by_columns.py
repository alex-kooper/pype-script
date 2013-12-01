"""
Sort records by specified columns. Each column described by a tuple:
(column_name, reverse) where reverse=True means descending order

It is supposed to be used in a pipline like this:

    pipeline_element | sort_by_columns('a', ('b', True), 'c') | pipeline_element
"""

from pype_script import sort

class RecordComparator(object):
    """
    A callable object that compares records by specified columns
    """
    def __init__(self, *args):
        def sort_descriptor(name, reverse=False):
            return (name, reverse)

        self.__args = [sort_descriptor(*d) for d in args]

    def __call__(self, record1, record2):
        for name, reverse in self.__args:
            res = cmp(record1.getattr(name), record2.getattr(name))

            if reverse:
                res = -res

            if res != 0:
                return res

        return 0

def sort_by_columns(*args):
    return sort(RecordComparator(*args))


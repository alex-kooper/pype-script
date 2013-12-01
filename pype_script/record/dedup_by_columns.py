"""
Remove duplicated records in the input stream based on a specified list of
columns

If more than one record in the input stream have equal values in the specified
columns only the first one is kept, all the subsequent records are skipped.

It is supposed to be used in a pipline like that:

    pipeline_element | dedup_by_columns(a', 'b', 'c') | pipeline_element ...
"""

from operator import attrgetter

from pype_script import dedup

def dedup_by_columns(*args):
    return dedup(key=attrgetter(*args))


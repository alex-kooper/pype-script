import itertools
from operator import add

class pmap(object):
    def __init__(self, function, input_iterable=None):
       self.function = function
       self.input_iterable = input_iterable

    def __iter__(self):
        return itertools.imap(self.function, self.input_iterable)

class pstar_map(object):
    def __init__(self, function, input_iterable=None):
       self.function = function
       self.input_iterable = input_iterable

    def __iter__(self):
        return itertools.starmap(self.function, self.input_iterable)

class pfilter(object):
    def __init__(self, predicate, input_iterable=None):
       self.predicate = predicate
       self.input_iterable = input_iterable
    
    def __iter__(self):
        return itertools.ifilter(self.predicate, self.input_iterable)

class pfilter_false(object):
    def __init__(self, predicate, input_iterable=None):
       self.predicate = predicate
       self.input_iterable = input_iterable
    
    def __iter__(self):
        return itertools.ifilterfalse(self.predicate, self.input_iterable)

class preduce(object):
    def __init__(self, function, initializer=None, input_iterable=None):
       self.function = function
       self.initializer = initializer
       self.input_iterable = input_iterable

       self.stopped = False

    def __iter__(self):
        self.stopped = False
        return self     
    
    def next(self):
        if(self.stopped):
            raise StopIteration

        self.stopped = True

        if self.initializer:
            return reduce(self.function, self.input_iterable, self.initializer)
        else:
            return reduce(self.function, self.input_iterable)

def psum(input_iterable=None):
    return preduce(add, None, input_iterable)

def pmin(input_iterable=None):
    return preduce(min, None, input_iterable)

def pmax(input_iterable=None):
    return preduce(max, None, input_iterable)

#class slice(FunctionWrapper):
#    def __init__(self, start, stop, step=1, input_iterator=None):
#       self.start = start
#       self.stop = stop
#       self.step = step
#
#       super(slice, self).__init__(input_iterator)
#
#    def _create_wrapped_iterator(self):
#        self._wrapped_iterator = itertools.islice(self.input_iterator, self.start, self.stop, self.step)


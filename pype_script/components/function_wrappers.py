import itertools

class map(object):
    def __init__(self, function, input_iterable=None):
       self.function = function
       self.input_iterable = input_iterable

    def __iter__(self):
        return itertools.imap(self.function, self.input_iterable)

class star_map(object):
    def __init__(self, function, input_iterable=None):
       self.function = function
       self.input_iterable = input_iterable

    def __iter__(self):
        return itertools.starmap(self.function, self.input_iterable)

class filter(object):
    def __init__(self, predicate, input_iterable=None):
       self.predicate = predicate
       self.input_iterable = input_iterable
    
    def __iter__(self):
        return itertools.ifilter(self.predicate, self.input_iterable)

class filter_false(object):
    def __init__(self, predicate, input_iterable=None):
       self.predicate = predicate
       self.input_iterable = input_iterable
    
    def __iter__(self):
        return itertools.ifilterfalse(self.predicate, self.input_iterable)


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


import itertools

from pype_script.chainable_iterator import FunctionWrapper

class map(FunctionWrapper):
    def __init__(self, function, input_iterator=None):
       self.function = function
       super(map, self).__init__(input_iterator)

    def _create_wrapped_iterator(self):
        self._wrapped_iterator = itertools.imap(self.function, self.input_iterator)

class star_map(FunctionWrapper):
    def __init__(self, function, input_iterator=None):
       self.function = function
       super(map, self).__init__(input_iterator)

    def _create_wrapped_iterator(self):
        self._wrapped_iterator = itertools.starmap(self.function, self.input_iterator)


class filter(FunctionWrapper):
    def __init__(self, predicate, input_iterator=None):
       self.predicate = predicate
       super(filter, self).__init__(input_iterator)

    def _create_wrapped_iterator(self):
        self._wrapped_iterator = itertools.ifilter(self.predicate, self.input_iterator)

class filter_false(FunctionWrapper):
    def __init__(self, predicate, input_iterator=None):
       self.predicate = predicate
       super(filter_false, self).__init__(input_iterator)

    def _create_wrapped_iterator(self):
        self._wrapped_iterator = itertools.ifilterfalse(self.predicate, self.input_iterator)

class slice(FunctionWrapper):
    def __init__(self, start, stop, step=1, input_iterator=None):
       self.start = start
       self.stop = stop
       self.step = step

       super(slice, self).__init__(input_iterator)

    def _create_wrapped_iterator(self):
        self._wrapped_iterator = itertools.islice(self.input_iterator, self.start, self.stop, self.step)


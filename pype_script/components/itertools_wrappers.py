import itertools

from pype_script.chainable_iterator import FunctionWrapper

class map(FunctionWrapper):
    def __init__(self, function, input_iterator=None):
       self.function = function
       super(map, self).__init__(input_iterator)

    def _create_iterator(self):
        self._wrapped_iterator = itertools.imap(self.function, self.input_iterator)


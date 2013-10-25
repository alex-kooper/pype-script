
class ChainableIterable(object):
    def __init__(self, input_iterable=None):
        self.input_iterable = input_iterable 


class FunctionWrapper(ChainableIterable):
    def __init__(self, input_iterable=None):
        super(FunctionWrapper, self).__init__(input_iterable)  

    def _create_wrapped_iterator(self):
        pass

    def next(self):
        return self._wrapped_iterator.next()


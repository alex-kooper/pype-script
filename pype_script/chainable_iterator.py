
class ChainableIterator(object):
    def __init__(self, input_iterator=None):
        self.input_iterator = input_iterator 

    def next():
        pass
        
    def __iter__(self):
        return self


class FunctionWrapper(ChainableIterator):
    def __init__(self, input_iterator=None):
        super(FunctionWrapper, self).__init__(input_iterator)  
        self._wrapped_iterator = None

    def __setattr__(self, name, value):
        super(FunctionWrapper, self).__setattr__(name, value)

        if name == 'input_iterator' and value:
            self._create_iterator()    

    def _create_wrapped_1iterator(self):
        pass

    def next(self):
        return self._wrapped_iterator.next()


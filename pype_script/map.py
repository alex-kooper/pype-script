
class map(IteratorChainer):
    def __init__(self, func):
        self.function = func

    def chain_iterator(self, input_iterator):
        return itertools.map(this.function, self.input_iterator)
        

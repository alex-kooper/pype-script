
class ClosableIteratorMixin(object):
    def close(self):
        try:
            self.input_iterator.close()
        except AttributeError:
            pass

class ClosableIteratorWrapper(ClosableIteratorMixin):
    def __init__(self, wrapped_iterator, input_iterator=None):
        self.wrapped_iterator = wrapped_iterator
        self.input_iterator = input_iterator

    def next(self):
        return self.wrapped_iterator.next()


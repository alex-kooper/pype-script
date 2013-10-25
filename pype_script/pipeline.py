
class Pipeline(object):
    def __init__(self, input_iterable):
        self.last_iterable = input_iterable

    def __or__(self, next_iterable):
        next_iterable.input_iterable = self.last_iterable
        self.last_iterable = next_iterable
        return self

    def __iter__(self):
        return iter(self.last_iterable)


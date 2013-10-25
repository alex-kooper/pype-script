
class Pipeline(object):
    def __init__(self, input_iterable):
        self.last_iterable = input_iterable

    def __or__(self, next_iterable):
        next_iterable.input_iterable = self.last_iterable
        return Pipeline(next_iterable)

    def __iter__(self):
        return iter(self.last_iterable)

iterate = Pipeline



class Pipeline(object):
    def __init__(self, first_iterable=None, last_iterable=None):
        self.first_iterable = self.last_iterable = first_iterable

        if last_iterable:
            self.last_iterable = last_iterable

    def __or__(self, next_iterable):
        next_iterable.input_iterable = self.last_iterable
        return Pipeline(self.first_iterable, next_iterable)

    def __iter__(self):
        return iter(self.last_iterable)

    def run(self):
        """ Iterate thorugh all the values and return the last one"""
        v = None

        for i in iter(self.last_iterable):
            v = i

        return v 

iterate = Pipeline


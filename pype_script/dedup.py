
class dedup(object):
    def __init__(self, key=None, input_iterable=None):
        if not key:
            key = lambda x: x

        self.key = key
        self.input_iterable = input_iterable

    def __iter__(self):
        self.__previous_keys = set()
        self.__input_iterator = iter(self.input_iterable)
        return self

    def next(self):
        el = self.__input_iterator.next()
        key = self.key(el)

        while key in self.__previous_keys:
            el = self.__input_iterator.next()
            key = self.key(el)

        self.__previous_keys.add(key)
        return el


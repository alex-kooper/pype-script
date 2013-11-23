
class dedup(object):
    """ Remove duplicated elements in the stream according to function key()

    If more than one elements that are equal according to function key() are in
    the stream, it leaves only the first one out of the series of equal 
    elements. If key function is not specified, it will compare objects
    """

    def __init__(self, key=None, input_iterable=None):
        if not key:
            key = lambda x: x

        self.key = key
        self.input_iterable = input_iterable

    def __iter__(self):
        return DedupIterator(self.key, iter(self.input_iterable))

class DedupIterator(object):
    def __init__(self, key, input_iterator):
        self.__key = key
        self.__input_iterator = input_iterator
        self.__previous_keys = set()

    def next(self):
        el = self.__input_iterator.next()
        key = self.__key(el)

        while key in self.__previous_keys:
            el = self.__input_iterator.next()
            key = self.__key(el)

        self.__previous_keys.add(key)
        return el

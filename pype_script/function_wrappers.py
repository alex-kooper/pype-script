import itertools
from operator import add

class pmap(object):
    def __init__(self, function, input_iterable=None):
       self.function = function
       self.input_iterable = input_iterable

    def __iter__(self):
        return itertools.imap(self.function, self.input_iterable)

class pstar_map(object):
    def __init__(self, function, input_iterable=None):
       self.function = function
       self.input_iterable = input_iterable

    def __iter__(self):
        return itertools.starmap(self.function, self.input_iterable)

class pfilter(object):
    def __init__(self, predicate, input_iterable=None):
       self.predicate = predicate
       self.input_iterable = input_iterable
    
    def __iter__(self):
        return itertools.ifilter(self.predicate, self.input_iterable)

class pfilter_false(object):
    def __init__(self, predicate, input_iterable=None):
       self.predicate = predicate
       self.input_iterable = input_iterable
    
    def __iter__(self):
        return itertools.ifilterfalse(self.predicate, self.input_iterable)

class preduce(object):
    def __init__(self, function, initializer=None, input_iterable=None):
       self.function = function
       self.initializer = initializer
       self.input_iterable = input_iterable

       self.stopped = False

    def __iter__(self):
        self.stopped = False
        return self     
    
    def next(self):
        if(self.stopped):
            raise StopIteration

        self.stopped = True

        if self.initializer:
            return reduce(self.function, self.input_iterable, self.initializer)
        else:
            return reduce(self.function, self.input_iterable)

def psum(input_iterable=None):
    return preduce(add, None, input_iterable)

def pmin(input_iterable=None):
    return preduce(min, None, input_iterable)

def pmax(input_iterable=None):
    return preduce(max, None, input_iterable)

class pslice(object):
    def __init__(self, *args):
        if len(args) > 3:
           self.input_iterable = args[3]
        else:
           self.input_iterable = None

        s = slice(*args[:3])
        self.start = s.start
        self.stop = s.stop
        self.step = s.step

    def __iter__(self):
        return itertools.islice(self.input_iterable, self.start, self.stop, self.step)

def take_first(n, input_iterable=None):
    return pslice(0, n, 1, input_iterable)

def skip_first(n, input_iterable=None):
    return pslice(n, None, 1, input_iterable)

class drop_while(object):
    def __init__(self, predicate, input_iterable=None):
       self.predicate = predicate
       self.input_iterable = input_iterable
    
    def __iter__(self):
        return itertools.dropwhile(self.predicate, self.input_iterable)

class take_while(object):
    def __init__(self, predicate, input_iterable=None):
       self.predicate = predicate
       self.input_iterable = input_iterable
    
    def __iter__(self):
        return itertools.takewhile(self.predicate, self.input_iterable)

class sort(object):
    def __init__(self, key=None, reverse=False, input_iterable=None):
        if not key:
            key = lambda x: x

        self.key = key
        self.reverse = reverse
        self.input_iterable = input_iterable

    def __iter__(self):
        return iter(sorted(self.input_iterable))
                                                                        
